
import os
import dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI

dotenv.load_dotenv()

prompt = ChatPromptTemplate.from_template("{query}")

llm = ChatOpenAI(
    model="gpt-4o",
    api_key=os.getenv("OPENAI_API_KEY"),
    base_url=os.getenv("OPENAI_API_BASE"),
    temperature=0.5,
)

# 3. 创建字符串输出解析器
parser = StrOutputParser()

# 4. 调用大语言模型生成解析结果
content = parser.invoke(llm.invoke(prompt.invoke({"query":"你好，你是?"})))

print(content)
