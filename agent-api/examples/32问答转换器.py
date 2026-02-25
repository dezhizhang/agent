import dotenv
from doctran import Doctran
from langchain_core.documents import Document
from langchain_community.document_transformers import DoctranQATransformer
from langchain_core.documents import Document
dotenv.load_dotenv()


_= Doctran

page_content = """
hello world

hello world
hello world
hello world

"""
documents = [Document(page_content=page_content)]

# 2. 构建问答转换器并转换
qa_transformer = DoctranQATransformer(openai_api_model="gpt-4o")
transformer_documents = qa_transformer.transform_documents(documents)

# 3. 输出内容

for qa in transformer_documents[0].metadata.get("questions_and_answers"):
    print(qa)


