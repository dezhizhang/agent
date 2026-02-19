import os

import dotenv
from operator import itemgetter
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langchain_core.runnables import RunnableParallel
from langchain_core.runnables import RunnablePassthrough


dotenv.load_dotenv()

def retrieveal(query:str) -> str:
    """一个摸拟的检索器函数"""
    print(f"正在检索：{query}")
    return "我是tom"

prompt = ChatPromptTemplate.from_template("""请根据用户的问题回答，可以参考对应的上下文进行生成。
<context>
{context}
</context>
用户的提问题：{query}""")

# 构建大语言模型
llm = ChatOpenAI(
    model="gpt-4o",
    api_key=os.getenv("OPENAI_API_KEY"),
    base_url=os.getenv("OPENAI_API_BASE"),
)

# 构建输出解析器
parser = StrOutputParser()

# 构建链
chain = RunnableParallel({
    "context":lambda x:retrieveal(x),
    "query":RunnablePassthrough(),
}) | prompt | llm | parser

# 调用链
# content = chain.invoke("你好，我是谁?")
content = chain.invoke({"query":"你好，我是谁"})

print(content)

