from typing import Type, Any
from langchain_core.tools import BaseTool
from pydantic import BaseModel,Field


class MultiplyInput(BaseModel):
    a:int = Field(description="第一个数字")
    b:int = Field(description="第二个数字")

class MultiplyTool(BaseTool):
    """乘法计算工具"""
    name: str = "multiply_tool"
    description: str = "将传递的两个数字相乘后返回"
    args_schema: Type[BaseModel] = MultiplyInput

    def _run(self, *args: Any, **kwargs: Any) -> Any:
        return kwargs["a"] * kwargs["b"]



calculator = MultiplyTool()

print("名字",calculator.name)
print("描述",calculator.description)
print("是否返回",calculator.return_direct)
print("方法调用",calculator.invoke({"a":2,"b":3}))
