import os
import dotenv

from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI

dotenv.load_dotenv()

# 1. 构建组件
prompt = ChatPromptTemplate.from_template("{query}")
llm = ChatOpenAI(
    model="gpt-4o",
    base_url=os.getenv("OPENAI_API_BASE"),
    api_key=os.getenv("OPENAI_API_KEY"),
)

parser = StrOutputParser()

chain = prompt | llm | parser

print(chain.invoke({"query":"请讲一个程序员的冷笑话"}))