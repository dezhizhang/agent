
import os

import dotenv
from  datetime import datetime
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI

dotenv.load_dotenv()

prompt = ChatPromptTemplate.from_messages([
    ("system", "你是OpenAI开发的聊天机器人,请回答用户的问题,现在的时间是{now}"),
    ("human", "{query}")
]).partial(now=datetime.now())

llm = ChatOpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),
    base_url=os.getenv("OPENAI_API_BASE"),
    model="gpt-4o",
    temperature=0.8,
)

response  = llm.stream(prompt.invoke({"query":"你能简单介绍一下LLM和LLMOps吗"}))

for chunk in response:
    print(chunk.content,flush=True,end="")