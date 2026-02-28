import dotenv
from langchain_openai import OpenAIEmbeddings

from langchain_community.vectorstores import Chroma

dotenv.load_dotenv()

embeddings = OpenAIEmbeddings(
    model="text-embedding-3-large"
)


chroma_db = Chroma(
    persist_directory="chroma_bge",
    embedding_function=embeddings,
    collection_name="shuqing",
    collection_metadata={"hnsw:space","cosine"}
)


query = "hello"
docs = chroma_db.similarity_search(query,k=2)

for doc in docs:
    print(doc.page_content)
    print("*" * 30)





