import json
import os

import dotenv
import requests
from langchain_core.tools import BaseTool
from pydantic import BaseModel, Field
from typing import Type,Any

dotenv.load_dotenv()




class GaodeWeatherArgsSchema(BaseModel):
    city: str = Field(description="需要查询天气预报目标城市，例如：广州")


class GaodeWeatherTool(BaseTool):
    """根据传入的城市名查询天气"""
    name:str = "gaode_weather"
    description:str = "当你想查询天气或者天气相关的问题时可以使用的工具"
    args_schema: Type[BaseModel] = GaodeWeatherArgsSchema

    def _run(self,*args:Any, **kwargs:Any) -> Any:
        """根据传入的城市名称运行调用api获取城市对应的天气预报信息"""
        try:
            # 1. 获取高德AP秘，如果没有创建的话创抛出错误
            gaode_api_key = os.getenv("GAODE_API_KEY")
            if not gaode_api_key:
                return f"高德开放平台API未配置"

            # 2. 从参数中获取city城市名字
            city = kwargs.get("city")
            api_domain = "https://restapi.amap.com/v3"
            session = requests.Session()

            # 3. 发起行政区编码查询，根据city获取ad_code
            city_response = session.request(
                method="GET",
                url=f"{api_domain}//config/district?city={gaode_api_key}&keywords={city}&subdistrict=0",
                headers={"Content-Type": "application/json;charset=utf-8"},
            )

            city_response.raise_for_status()
            city_data = city_response.json()

            if city_data.get("info") == "OK":
                ad_code = city_data['districts'][0]['ad_code']
                weather_response = session.request(
                    method="GET",
                    url=f"{api_domain}/weather/weatherInfo?key={gaode_api_key}&city={ad_code}&extensions=all",
                )

                weather_response.raise_for_status()
                weather_data = weather_response.json()

                if weather_data.get("info") == "OK":
                    return json.dumps(weather_data)
            return f"获取{city}天气预报失败"
        except Exception as e:
            return f"获取{kwargs.get('city')}天气预报失败{e}"

gaode_weather = GaodeWeatherTool()
print(gaode_weather.invoke({"city":"广州"}))






