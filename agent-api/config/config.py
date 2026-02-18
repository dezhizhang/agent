
import os
from typing import Any
from .defalt_config import DEFAULT_CONFIG

def _get_env(key:str) -> Any:
    """从环境变量中获取配置项，如果找不到则返回默认值"""
    return os.getenv(key,DEFAULT_CONFIG.get(key))

def _get_bool_env(key:str) -> bool:
    """从环境变量中获取布尔值的配置项，如果找不到则返回默认值"""
    value :str = _get_env(key)
    return value.lower() == "true" if value is not None else False



class Config:
    def __init__(self):
        """关闭wtf的csrf保护"""
        self.SECRET_KEY = os.getenv("SECRET_KEY")
        self.WTF_CSRF_ENABLED = False
        self.SQLALCHEMY_ENGINE_OPTIONS={
            "pool_size": 30,
            "pool_recycle": 3600,
        }
        self.SQLALCHEMY_ECHO = True
