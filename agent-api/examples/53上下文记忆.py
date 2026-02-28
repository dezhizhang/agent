import dotenv
from langchain_classic.retrievers.document_compressors import LLMChainExtractor
from langchain_openai import ChatOpenAI,OpenAIEmbeddings
from langchain_classic.retrievers.contextual_compression import ContextualCompressionRetriever
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

compressor = LLMChainExtractor.from_llm(llm)
retriever = ContextualCompressionRetriever(base_compressor=compressor,base_retriever=chroma_db.as_retriever())

docs = retriever.invoke("hello world")

for doc in docs:
    print(doc.page_content)
    print("*" * 30)


