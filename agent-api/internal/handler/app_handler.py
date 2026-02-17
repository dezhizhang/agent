import os
from flask import request
from openai import OpenAI
from internal.schema.app_schema import CompletionReq
from pkg.response import success_json,validate_error_json
from internal.exception import FailException


class AppHandler:
    """应用控制器"""

    def completion(self):
        """聊天接口"""
        # 1. 提取从接口中获取输入
        query = request.json.get('query')
        # 2. 构建openai客户端，并发起请求
        client = OpenAI(
            api_key=os.getenv("OPENAI_API_KEY"),
            base_url=os.getenv("OPENAI_API_BASE"),
        )
        req = CompletionReq()
        if not req.validate():
            return validate_error_json(req.errors)
        # 3. 得到请求响应，然后将OpenAI的响应传给前前端
        completion = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role":"system","content":"你是OpenAI开发的聊天机器人，请根据用户的输入回复对应的信息"},
                {"role":"user","content":query},
            ]
        )

        content = completion.choices[0].message.content


        return success_json({"content":content})


    def ping(self):
        raise FailException("数据异常")
        # return {"ping": "pong"}