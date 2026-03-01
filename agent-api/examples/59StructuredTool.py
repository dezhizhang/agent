from langchain_core.tools import StructuredTool
from pydantic import BaseModel, Field
from typing import Optional


class BankAccountQuery(BaseModel):
    account_id: str = Field(description="用户的银行账号")
    start_date: Optional[str] = Field(description="查询开始日期")
    end_date: Optional[str] = Field(description="查询结束日期")
    query_type: str = Field(
        default="balance",
        description=""
    )


def query_bank_account(
        account_id: str,
        start_date: Optional[str] = None,
        end_date: Optional[str] = None,
        query_type: str = "balance",
) -> str:
    """"查询银行帐户信息"""

    if query_type == "balance":
        return f"帐户{account_id}当前余额为:￥100.00"
    elif query_type == "transactions":
        if start_date and end_date:
            return f"帐户:{account_id}在{start_date}到:{end_date}之间有5笔交易"
        else:
            return f"帐户:{account_id}最近有9笔交易"
    elif query_type == "interest_rate":
        return f"帐户:{account_id}的当前利率为1.5%"
    else:
        return "不支持查询类型"

bank_tool = StructuredTool.from_function(
    func=query_bank_account,
    name="query_bank_account",
    description="查询银行帐户信息",
    args_schema=BankAccountQuery,
)

print(bank_tool.args_schema.model_json_schema())


result = bank_tool.invoke({
    "account_id": "123",
    "start_date": "2021-09-01",
    "end_date": "2021-09-30",
    "query_type": "balance",
})

print(result)



