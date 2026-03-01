
from langchain_core.tools import tool
from pydantic import BaseModel,Field



class CityModel(BaseModel):
    city:str = Field(..., description="城市名称")



@tool(description="获取城市的天气信息",args_schema=CityModel)
def get_weather(city:str) -> str:
    """获取城市的天气信息"""
    return "It's sunny in" + city

print(get_weather.name)
print(get_weather.description)
print(get_weather.args)


