from flask import Flask

from internal.exception import CustomException
from internal.router import Router
from config import Config
from pkg.response import json,Response,HttpCode

class Http(Flask):
    """http服务引擎"""
    def __init__(self, *args,conf:Config,router:Router, **kwargs):
        # 1.调用父类构造函数初始化
        super().__init__(*args, **kwargs)
        # 2. 初始化应用配置
        self.config.from_object(conf)
        # 3. 注册绑定异常错误处理
        self.register_error_handler(Exception,self._register_error_handler)
        # 4. 注册应用路由
        router.register_router(self)

    def _register_error_handler(self,error:Exception):
        """<UNK>"""
        # 1. 判断异常信息是否是自定义异常，如果是可以提交message和code等信息
        if isinstance(error,CustomException):
            return json(Response(
                code=error.code,
                message=error.message,
                data=error.data if error.data is not None else {},
            ))

        # 2. 如果不是我们自定的异常，刚有可能是程序，数据库抛出的异常，也可以提取信息
        return json(Response(
            code=HttpCode.FAIL,
            message=str(error),
            data={}
        ))


