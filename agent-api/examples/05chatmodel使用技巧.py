import os
from datetime import datetime

import dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI,OpenAI

dotenv.load_dotenv()

# 1. 提示词
prompt = ChatPromptTemplate.from_messages([
    ("system", "你是OpenAI开发的聊天机器人,请回答用户的问题,现在的时间是{now}"),
    ("human", "{query}")
]).partial(now=datetime.now())

llm = ChatOpenAI(
    model="gpt-4o",
    temperature=0.7,
    api_key=os.getenv("OPENAI_API_KEY"),
    base_url=os.getenv("OPENAI_API_BASE"),
)

response = llm.invoke(prompt.invoke({"query":"现在是几点,请讲一个程序员的冷笑话"}))

print(response.content)


