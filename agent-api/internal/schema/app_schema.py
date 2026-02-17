from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired, Length


class CompletionReq(FlaskForm):
    """基础聊天接口请求验证"""
    query = StringField('query', validators=[
        DataRequired(message="用户的提问是必填"),
        Length(max=2000, message="最大只能输入2000字符")
    ])