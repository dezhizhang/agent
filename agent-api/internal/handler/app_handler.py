import os
from flask import request

from internal.schema.app_schema import CompletionReq
from pkg.response import success_json,validate_error_json
from internal.exception import FailException
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser

class AppHandler:
    """应用控制器"""

    def completion(self):
        """聊天接口"""
        # 1. 提取从接口中获取输入
        req = CompletionReq()
        if not req.validate():
            return validate_error_json(req.errors)

        # 构建提示词模板
        prompt = ChatPromptTemplate.from_template("{query}")

        # 2. 构建openai客户端，并发起请求
        llm = ChatOpenAI(
            model="gpt-4o",
            api_key=os.getenv("OPENAI_API_KEY"),
            base_url=os.getenv("OPENAI_API_BASE"),
        )

        parser = StrOutputParser()

        # 3. 构建链
        chain = prompt | llm | parser

        content = chain.invoke({"query":req.query.data})

        return success_json({"content":content})


    def ping(self):
        raise FailException("数据异常")
        # return {"ping": "pong"}