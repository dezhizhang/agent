import os

import dotenv
from pydantic import BaseModel,Field
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
dotenv.load_dotenv()

class Joke(BaseModel):
    # 冷笑话
    joke:str = Field(description="回答用户的冷笑话")
    # 冷笑话的笑点
    punchline:str = Field(description="这个冷笑话的笑点")

parser = JsonOutputParser(pydantic_object=Joke)

prompt = ChatPromptTemplate.from_template(
    "请根据用户的提问进行回答。\n{format_instructions}\n{query}",
    partial_variables={
        "format_instructions": parser.get_format_instructions()
    }
)

llm = ChatOpenAI(
    model="gpt-4o",
    api_key=os.getenv("OPENAI_API_KEY"),
    base_url=os.getenv("OPENAI_API_BASE"),
)

response = parser.invoke(llm.invoke(prompt.invoke({"query":"请讲一个关于程序员的冷笑话"})))
print(response)
