from langchain_core.tools import BaseTool
from langchain_community.utilities import GoogleSerperAPIWrapper
from langchain_community.tools import GoogleSerperRun
from pydantic import BaseModel,Field

class GoogleSerperArgsSchema(BaseModel):
    """谷歌SerperAPI搜索参数描述"""
    query:str = Field(description="需要检索查询的语句")


def google_serper(**keywords) -> BaseTool:
    """谷歌Serper搜索"""
    return  GoogleSerperRun(
        name='google_serper',
        description='这是一个低成本的谷歌搜索API。当你需要搜索时事时候，可以使用该工具',
        args_schema=GoogleSerperArgsSchema,
        api_wrapper=GoogleSerperAPIWrapper()
    )
