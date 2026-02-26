from langchain_community.tools import GoogleSerperRun
from pydantic import BaseModel,Field
import dotenv
from langchain_community.utilities import GoogleSerperAPIWrapper
dotenv.load_dotenv()



class GaodeWeatherArgsSchema(BaseModel):
    query: str = Field(description="执行谷哥搜索查询语句")

google_search = GoogleSerperRun(
    name="google_search",
    description="谷哥搜索查询语句",
    argschema=GaodeWeatherArgsSchema,
    api_wrapper=GoogleSerperAPIWrapper(),
)

print(google_search.invoke("tom"))

