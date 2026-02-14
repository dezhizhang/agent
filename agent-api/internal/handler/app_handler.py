
from flask import request
from openai import OpenAI

class AppHandler:
    """应用控制器"""

    def completion(self):
        """聊天接口"""
        # 1. 提取从接口中获取输入
        query = request.json.get('query')
        # 2. 构建openai客户端，并发起请求
        client = OpenAI(api_key='sk-zUDelHgZPjOX4eP3tnTcVXRC9cgA8yerufoOMyeM7V9Hx9GM',base_url="https://poloai.top/v1")
        # 3. 得到请求响应，然后将OpenAI的响应传给前前端
        completion = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role":"system","content":"你是OpenAI开发的聊天机器人，请根据用户的输入回复对应的信息"},
                {"role":"user","content":query},
            ]
        )
        return completion.choices[0].message.content



    def ping(self):
        return {"ping": "pong"}