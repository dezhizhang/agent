from langchain_core.vectorstores import InMemoryVectorStore
from langchain_openai import OpenAIEmbeddings
from langchain_community.document_transformers import LongContextReorder
import dotenv

dotenv.load_dotenv()

embeddings = OpenAIEmbeddings(
    model="text-embedding-3-large",
)

texts = [
    "篮球是一项很棒的运动。",
    "《Flymetothemoon》是我最喜欢的歌曲之一。",
    "凯尔特人队是我最喜欢的球队。",
    "这是一篇关于波士顿凯尔特人队的文档。",
    "我特别喜欢去看电影。",
    "波士顿凯尔特人队以20分的优势赢得了比赛。",
    "这只是一个随机文本。",
    "《艾尔登法环》是过去15年中最好的游戏之一。",
    "L·科内特是凯尔特人队最好的球员之一。",
    "拉里·伯德是一位标志性的NBA球员。"
]

retriever = InMemoryVectorStore.from_texts(texts, embedding=embeddings).as_retriever(
    search_kwargs={"k": 5}
)

query ="你能告诉我关于凯尔特人队的哪些信息?"

docs = retriever.invoke(query)

for doc in docs:
    print(f"-{doc.page_content}")

print("*" * 50)

reorder = LongContextReorder()
reorder_docs = reorder.transform_documents(docs)


for doc in reorder_docs:
    print(f"->{doc.page_content}")


