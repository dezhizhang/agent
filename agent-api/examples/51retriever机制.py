

import dotenv
from langchain_openai import OpenAIEmbeddings
from langchain_chroma import Chroma

dotenv.load_dotenv()

embeddings = OpenAIEmbeddings(
    model="text-embedding-3-large"
)
chroma_db = Chroma(
    persist_directory="chroma_bge",
    embedding_function=embeddings,
    collection_name="shuqing",
)

retriever = chroma_db.as_retriever()

docs = retriever.invoke("hello world")

for doc in docs:
    print(doc.page_content)
    print("*" * 30)

