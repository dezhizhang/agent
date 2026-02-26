import dotenv
from langchain_community.tools import GoogleSerperRun
from langchain_community.tools.openai_dalle_image_generation import OpenAIDALLEImageGenerationTool
from langchain_community.utilities import GoogleSerperAPIWrapper
from langchain_community.utilities.dalle_image_generator import DallEAPIWrapper
from pydantic import BaseModel,Field
from langchain_openai import ChatOpenAI
from langchain.agents import create_agent

dotenv.load_dotenv()

class GoogleSerperArgsSchema(BaseModel):
    query:str = Field(description="执行谷歌搜索查询语句")
    pass

class DallEargsSchema(BaseModel):
    query: str = Field(description="输入应该是生成图像文本提示(prompt)")

# 1. 定义工具与工具列表
google_Serper = GoogleSerperRun(
    name="google_serper",
    description="一个低成本的谷歌搜索API",
    args_schema = GoogleSerperArgsSchema,
    api_wrapper=GoogleSerperAPIWrapper(),
)

dalle= OpenAIDALLEImageGenerationTool(
    name="openai_dalle",
    api_wrapper=DallEAPIWrapper(model="gpt-image-1"),
    args_schema=DallEargsSchema,
)
tools = [google_Serper, dalle]

model = ChatOpenAI(
    model="gpt-4o",
)

agent = create_agent(
    model=model,
    tools=tools,
)

print(agent.invoke({"messages":[("human","请我帮我绘制一张小乌")]}))
