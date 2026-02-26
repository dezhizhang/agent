from langchain_core.tools import StructuredTool
from pydantic import BaseModel,Field


class MultiplyInput(BaseModel):
    a:int = Field(description="第一个数字")
    b:int = Field(description="第二个数字")


def multiply(a:int, b:int) -> int:
    """将传递的两个数字相乖"""
    return a * b

async def amultiply(a:int, b:int) -> int:
    """将传递的两个数字相乖"""
    return a * b


calculator = StructuredTool.from_function(
    func=multiply,
    coroutine=amultiply,
    name="multiply_tool",
    description="将传递的两个数字相乖",
    return_direct=True,
    args_schema=MultiplyInput,
)

print("名字",calculator.name)
print("描述",calculator.description)
print("是否返回",calculator.return_direct)
print("方法调用",calculator.invoke({"a":2,"b":3}))

