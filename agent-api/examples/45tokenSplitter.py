from langchain_text_splitters import TokenTextSplitter
import tiktoken

text = "LangChain 是一个用于构建基于大语言模型（LLM）应用的开发框架，它把提示词管理、模型调用、数据检索、工具调用和多步骤流程等能力模块化，让开发者可以像搭积木一样快速搭建 AI 聊天机器人、知识库问答系统和自动化 Agent 应用，本质上相当于 AI 时代的应用开发框架，大幅降低了把模型能力落地成产品的难度。"

text_splitter = TokenTextSplitter(
    encoding_name="cl100k_base",
    chunk_size=30,
    chunk_overlap=5
)

enc = tiktoken.get_encoding("cl100k_base")

chunks = text_splitter.split_text(text)

for i,chunk in enumerate(chunks):
    print(f"文本块{i + 1}:{chunk}")
    print(f"token数量:{len(enc.encode(chunk))}")



