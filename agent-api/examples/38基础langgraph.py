from typing import TypedDict, Annotated, Any
import dotenv
from langchain_openai import ChatOpenAI
from langgraph.graph.message import add_messages
from langgraph.graph import StateGraph, START, END
from langchain_core.runnables import RunnableConfig

dotenv.load_dotenv()

llm = ChatOpenAI(model="gpt-4o")


class State(TypedDict):
    """图结构的状态数据"""
    messages: Annotated[list, add_messages]


def chatbot(state: State, config: RunnableConfig) -> Any:
    """聊天机器人"""
    ai_message = llm.invoke(state["messages"], config=config)
    return {"messages": [ai_message]}


graph_builder = StateGraph(State)

graph_builder.add_node("llm", chatbot)
graph_builder.add_edge(START, "llm")
graph_builder.add_edge("llm", END)

graph = graph_builder.compile()

print(
    graph.invoke(
        {"messages": [("human", "你好，你是谁，我是tom，我喜欢跑步")]}
    )
)