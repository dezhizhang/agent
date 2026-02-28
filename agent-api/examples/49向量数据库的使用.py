import dotenv

from langchain_community.document_loaders import TextLoader
from langchain_openai import OpenAIEmbeddings
from langchain_text_splitters import CharacterTextSplitter

from langchain_community.vectorstores import Chroma



dotenv.load_dotenv()

loader = TextLoader("../memory.txt",encoding="utf-8")

documents = loader.load()

text_splitter = CharacterTextSplitter(
    separator="\n",
    chunk_size=15,
    chunk_overlap=0
)

docs = text_splitter.split_documents(documents)



embeddings = OpenAIEmbeddings(
    model="text-embedding-3-large"
)


persist_dir = "chroma_bge"
db = Chroma.from_documents(docs,embeddings,collection_name="shuqing",persist_directory=persist_dir)




