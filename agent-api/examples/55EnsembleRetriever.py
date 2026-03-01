import dotenv
from langchain_classic.retrievers import EnsembleRetriever
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_chroma import Chroma


dotenv.load_dotenv()



doc_list_1 = [
    "张三喜欢苹果",
    "李四喜欢橘子",
    "苹果和橘子都是水果",
    "苹果的果肉又脆又多汁,有酸甜的味道。",
    "苹果含有膳食纤维果胶和抗氧化剂如维生素C",
    "苹果和橘子都是水果,但是苹果的果肉更甜,而橘子的果肉更酸",
    "苹果和橘子都是水果但是苹果含有膳食纤维果胶)和抗氧化剂,如维生素C而橘子没有。",
]

doc_list_2 = [
    "王五喜欢苹果",
    "赵六喜欢橘子",
    "苹果呈圆形,表皮光滑,通常呈红色、绿色或黄色",
    "在多元文化中,苹果象征着健康和知识",
    "苹果可以生吃,也可以煮成美味的甜点,还可以榨成果汁"
]

embeddings = OpenAIEmbeddings(
    model="text-embedding-3-large",
)

db1 = Chroma.from_texts(doc_list_1, embeddings, metadatas=[{"source": 1}] * len(doc_list_1),
                        persist_directory="chroma_db_1")
db2 = Chroma.from_texts(doc_list_2, embeddings, metadatas=[{"source": 2}] * len(doc_list_2),
                        persist_directory="chroma_db_2")


retriever1 = db1.as_retriever()
retriever2 = db2.as_retriever()

ensemble_retriever = EnsembleRetriever(
    retrievers=[retriever1, retriever2],
    weights=[0.5,0.5]
)

docs = ensemble_retriever.invoke("谁喜欢苹果")


for doc in docs:
    print(doc.page_content)




