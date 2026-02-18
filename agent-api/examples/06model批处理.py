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

ai_messages = llm.batch([
    prompt.invoke({"query":"你好，你是?"}),
    prompt.invoke({"query":"请讲一个关于程序员的冷笑话?"}),
])


for ai_message in ai_messages:
    print(ai_message.content)