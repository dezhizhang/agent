import dotenv
import numpy as np
from sklearn.metrics.pairwise import  cosine_similarity
from langchain_openai import OpenAIEmbeddings

dotenv.load_dotenv()


embeddings = OpenAIEmbeddings(
    model="text-embedding-3-large"
)

text1 = "猫在垫子上"
text2 = "执子上有一只猫"
text1_vector = embeddings.embed_query(text1)
text2_vector = embeddings.embed_query(text2)

text1_vector = np.array(text1_vector).reshape(1,-1)
text2_vector = np.array(text2_vector).reshape(1,-1)

similarity = cosine_similarity(text1_vector, text2_vector)[0][0]

print(similarity)



