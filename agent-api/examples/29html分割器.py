from langchain_text_splitters import HTMLHeaderTextSplitter

# 1 构建文本与分割标题
html_string = """"""
headers_to_split_on=[]

# 2. 创建分割器并分割
text_splitter = HTMLHeaderTextSplitter(headers_to_split_on)
chunks = text_splitter.split_text(html_string)

# 3. 输出分割内容
for chunk in chunks:
    print("chunk",chunk)

