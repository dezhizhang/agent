import asyncio
from typing import Optional, Any, Coroutine
from langchain_core.callbacks import AsyncCallbackManagerForToolRun, CallbackManagerForToolRun
from langchain_core.tools import BaseTool
from langchain_core.tools.base import ArgsSchema
from pydantic import BaseModel, Field


class CalculatorInput(BaseModel):
    a: int = Field(description="first number")
    b: int = Field(description="second number")


class CustomCalculatorTool(BaseTool):
    name: str = "Calculator"
    description: str = "useful for when you need to answer questions about math"
    args_schema: Optional[ArgsSchema] = CalculatorInput

    def _run(self, a: int, b: int, run_manager: Optional[CallbackManagerForToolRun] = None) -> int:
        """Use the tool"""
        return a * b

    async def _arun(self, a: int, b: int, run_manager: Optional[AsyncCallbackManagerForToolRun] = None):
        """Use the tool asynchronously"""
        return self._run(a, b, run_manager=run_manager.get_sync())

multipy = CustomCalculatorTool()
print(multipy.args_schema.model_json_schema())
print(multipy.invoke({"a":2, "b":3}))
