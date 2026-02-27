from typing import TypedDict,Annotated,Any,Literal
import dotenv
from langchain_community.tools import GoogleSerperRun
from langchain_community.tools.openai_dalle_image_generation import OpenAIDALLEImageGenerationTool
from langchain_community.utilities import GoogleSerperAPIWrapper
from langchain_community.utilities.dalle_image_generator import DallEAPIWrapper
from pydantic import BaseModel,Field
from langchain_openai import ChatOpenAI
from langgraph.checkpoint.memory import MemorySaver
from langgraph.graph import START,END,StateGraph
from langgraph.graph.message import add_messages
from langgraph.prebuilt import ToolNode
from langchain_core.runnables import RunnableConfig

dotenv.load_dotenv()

class GoogleSerperArgsSchema(BaseModel):
    query:str = Field(description="执行谷歌搜索的查询语句")


class DallEArgsSchema(BaseModel):
    query:str = Field(description="输入应该是生成图像的文本提示(prompt)")

google_serper = GoogleSerperRun(
    name="google_serper",
    description="一个低成本的谷歌搜索API",
    args_schema=GoogleSerperArgsSchema,
    api_wrapper=GoogleSerperAPIWrapper()   # ← 加 ()
)

dalle = OpenAIDALLEImageGenerationTool(
    name="dalle",
    api_wrapper=DallEAPIWrapper(model="gpt-4o-image"),
    args_schema=DallEArgsSchema
)

class State(TypedDict):
    """图状态数结构,类型为字典"""
    messages:Annotated[list,add_messages]

tools = [google_serper,dalle]
llm = ChatOpenAI(model="gpt-4o")
llm_with_tools = llm.bind_tools(tools)


def chatbot(state: State, config: RunnableConfig | None = None):
    ai_message = llm_with_tools.invoke(state["messages"], config=config)
    return {"messages": [ai_message]}

def route(state:State,config:RunnableConfig) -> Literal["tools","__end__"]:
    ai_message = state["messages"][-1]

    if hasattr(ai_message,"tools_calls") and callable(ai_message.tools) > 0:
        return "tools"

    return END

graph_builder = StateGraph(State)

# 添加节点
graph_builder.add_node("llm",chatbot)
graph_builder.add_node("tools",ToolNode(tools=tools))

graph_builder.add_edge(START,"llm")
graph_builder.add_edge("tools","llm")
graph_builder.add_conditional_edges("llm",route)


checkpointer = MemorySaver()
graph = graph_builder.compile(checkpointer=checkpointer,interrupt_after=["tools"])

config = {"configurable":{"thread_id":1}}
state = graph.invoke(
    {"messages":[("human","2026的会有那些新科技突破")]},
    config=config
)


# 获取人类的提示
if hasattr(state["messages"][-1],"tool_calls") and len(state["messages"][-1].tool_calls) > 0:
    tool_calls = state["messages"][-1].tool_calls
    human_input = input("如需调用工具请回复yes否则回复no")
    if human_input.lower() == "yes":
        print(graph.invoke(None,config))
    else:
        print("图程序执行结束")









