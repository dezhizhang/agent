from pydantic import BaseModel


class ToolEntity(BaseModel):
    """工具实体类，存储的信息映射的工具名.yaml里的数据"""
    name: str
    label: str
    description: str
    params:list = [] # 工具的参数信息
    
