import dotenv
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_chroma import Chroma

dotenv.load_dotenv()

embeddings = OpenAIEmbeddings(
    model="text-embedding-3-large",
)

chroma_db = Chroma(
    persist_directory="chroma_bge",
    embedding_function=embeddings,
    collection_name="shuqing"
)

llm = ChatOpenAI(
    model="gpt-4o"
)

retriever = chroma_db.as_retriever(
    search_type="similarity_score_threshold",
    search_kwargs={"score_threshold": 0.45},
)

docs = retriever.invoke("hello world")

for doc in docs:
    print(doc.page_content)

