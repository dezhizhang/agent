import os

import dotenv
from langchain_core.tools import BaseTool
from pydantic import BaseModel, Field
from typing import Type,Any

dotenv.load_dotenv()




class GaodeWeatherArgsSchema(BaseModel):
    city: str = Field(description="需要查询天气预报目标城市，例如：广州")


class GaodeWeatherTool(BaseTool):
    """根据传入的城市名查询天气"""
    name = "gaode_weather"
    description = "当你想查询天气或者天气相关的问题时可以使用的工具"
    args_schema: Type[BaseModel] = GaodeWeatherArgsSchema

    def _run(self,*args:Any, **kwargs:Any) -> Any:
        """根据传入的城市名称运行调用api获取城市对应的天气预报信息"""
        # 1. 获取高德AP秘，如果没有创建的话创抛出错误
        gaode_api_key = os.getenv("GAODE_API_KEY")
        if not gaode_api_key:
            return f"高德开放平台API未配置"

        #

        pass



