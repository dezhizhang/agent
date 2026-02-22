import os
import numpy as np
import dotenv
from numpy.linalg import  norm
from langchain_openai import OpenAIEmbeddings

dotenv.load_dotenv()


def cosine_similarity(vec1:list, vec2:list) -> float:
    """计算传入两个向量的余弦相拟度"""
    # 1. 计算两个向量的点积
    dot_product = np.dot(vec1, vec2)

    # 2. 计算向量的长度
    vec1_norm = norm(vec1)
    vec2_norm = norm(vec2)

    # 3. 计算余弦相拟度
    return dot_product / (vec1_norm * vec2_norm)


embeddings = OpenAIEmbeddings(
    api_key=os.getenv("OPENAI_API_KEY"),
    base_url=os.getenv("OPENAI_API_BASE"),
    model="text-embedding-3-small"
)

query_vector = embeddings.embed_query("你好我叫tom")

document_vector = embeddings.embed_documents([
    "你好，我叫tom，我喜欢跑步",
    "这个喜欢跑步的人叫tom",
    "哈哈，我是tom"
])

# 计算余弦相拟度
print("向量1和向2相拟度",cosine_similarity(document_vector[0],document_vector[1]))
print("向量1和向量3相似度",cosine_similarity(document_vector[0],document_vector[2]))




