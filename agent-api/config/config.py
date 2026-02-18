
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
        self.WTF_CSRF_ENABLED = False
        self.SECRET_KEY = _get_env("SECRET_KEY")
        self.SQLALCHEMY_ENGINE_OPTIONS={
            "pool_size": _get_env("SQLALCHEMY_POOL_SIZE"),
            "pool_recycle": _get_env("SQLALCHEMY_POOL_RECYCLE"),
        }
        self.SQLALCHEMY_ECHO = _get_bool_env("SQLALCHEMY_ECHO")
        self.SQLALCHEMY_DATABASE_URI = _get_env("SQLALCHEMY_DATABASE_URI")