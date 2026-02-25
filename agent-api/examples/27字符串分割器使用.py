from langchain_community.document_loaders import UnstructuredFileLoader
from langchain_text_splitters import CharacterTextSplitter

#1. 加载对应的文档

loader = UnstructuredFileLoader("./README.md")
documents = loader.load()

# 创建文本分割器
text_splitter = CharacterTextSplitter(
    separator="\n\n",
    chunk_size=500,
    chunk_overlap=50
)

# 3. 分割文本
chunks = text_splitter.split_documents(documents)
for chunk in chunks:
    print(f"块大小{len(chunk.page_content)}")
