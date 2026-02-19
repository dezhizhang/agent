import os

import dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_openai import ChatOpenAI
from langchain_core.callbacks import StdOutCallbackHandler

dotenv.load_dotenv()


class LLMOpsCallbackHandler(StdOutCallbackHandler):
    """自定义LLMOps回调函数"""
    def on_chat_model_start(self,):

prompt = ChatPromptTemplate.from_template("{query}")

# 2 创建大语言模型
llm = ChatOpenAI(
    model="gpt-4o",
    api_key=os.getenv("OPENAI_API_KEY"),
    base_url=os.getenv("OPENAI_API_BASE"),
    temperature=0.8
)

# 构建链
chain = {"query":RunnablePassthrough()} | prompt | llm | StrOutputParser()

# 调用链并执行
content = chain.invoke("你好，你是?",config={"callbacks":[StdOutCallbackHandler()]})

print(content)

