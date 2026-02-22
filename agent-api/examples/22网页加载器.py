from langchain_community.document_loaders import WebBaseLoader

loader = WebBaseLoader("https://aint.top/")
document = loader.load()

print(document)
print(len(document))
print(document[0].metadata)
