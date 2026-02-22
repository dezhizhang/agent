import dotenv
from langchain_openai import OpenAIEmbeddings
from langchain_classic.storage import LocalFileStore
from langchain_classic.embeddings import CacheBackedEmbeddings
import numpy as np
from numpy.linalg import norm

dotenv.load_dotenv()


embeddings = OpenAIEmbeddings(model="text-embedding-3-small")

def cosine_similarity(vector1:list, vector2:list):
    """计算传入两个向量的余弦相似度"""
    # 1. 计算内积/点积
    dot_product = np.dot(vector1,vector2)

    # 2.计算向量的范数/长度
    norm_vec1 = norm(vector1)
    norm_vec2 = norm(vector2)

    # 3. 计算余弦相似度
    return dot_product / (norm_vec1 * norm_vec2)

# 1️⃣ 创建真实 Embeddings 实例
embeddings = OpenAIEmbeddings(model="text-embedding-3-small")

# 2️⃣ 用 CacheBackedEmbeddings 包装
embeddings_with_cache = CacheBackedEmbeddings.from_bytes_store(
    embeddings,
    LocalFileStore("./cache/"),
    namespace="text-embedding-3-small",
    query_embedding_cache=True,
)

# 3️⃣ 测试 embed_query / embed_documents
query_vector = embeddings_with_cache.embed_query("你好，我是tom,我喜欢跑步")
documents_vector = embeddings_with_cache.embed_documents([
    "你好，我叫tom，我喜欢跑步",
    "这个喜欢跑步的人叫tom",
    "哈哈，我是tom"
])

print(query_vector)
print(len(query_vector))






