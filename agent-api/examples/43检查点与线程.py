import dotenv
from langchain_openai import ChatOpenAI
from langchain.agents import create_agent
from langgraph.checkpoint.memory import MemorySaver

dotenv.load_dotenv()

checkpointer = MemorySaver()

agent = model = create_agent(
    model="gpt-4o",
    tools=[],
    checkpointer=checkpointer,
)

print(agent.invoke(
    {"messages": [("human", "你好，我是tom")]},
    config={"configurable":{"thread_id":1}}
))

print(agent.invoke({"messages": [("human", "你知道我叫什么吗")]},config={"configurable":{"thread_id":1}}))
