from flask import Flask
from internal.router import Router
from config import Config


class Http(Flask):
    """http服务引擎"""
    def __init__(self, *args,config:Config,router:Router, **kwargs):
        super().__init__(*args, **kwargs)
        # 注册应用路由
        router.register_router(self)
        self.config.from_object(config)
