from langchain_community.document_loaders import UnstructuredMarkdownLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

loader = UnstructuredMarkdownLoader("./README.md")

document = loader.load()

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50,
    add_start_index=True
)

chunks = text_splitter.split_documents(document)
for chunk in chunks:
    print(f"块大小{len(chunk.page_content)} 元数据:{chunk.metadata}")

