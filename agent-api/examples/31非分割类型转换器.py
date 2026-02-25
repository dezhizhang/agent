import jieba.analyse
from typing import List
from langchain_unstructured import UnstructuredLoader

from langchain_text_splitters import TextSplitter

class CustomTextSplitter(TextSplitter):
    """自定义分割器"""
    def __init__(self, seperator:str,top_k:int = 10,**kwargs):
        """构造函数，传递分割器还有需要提取的关急需词数，默认为10"""
        super().__init__(**kwargs)
        self._seperator = seperator
        self._top_k = top_k

    def split_text(self,text:str) -> List[str]:
        """传递对应的文本执行分割数据关键词，组成文档列表返回"""
        # 1. 根据传递的分割传入的文本
        split_texts = text.split(self._seperator)

        # 2. 提取分割出来的每一段文本的关键词，数量为
        text_keywords = []
        for split_text in split_texts:
          text_keywords.append(jieba.analyse.extract_tags(split_text,self._top_k))

        # 3. 将关键词使用逗号进行拼接组成字符串列表
        return [",".join(keywords) for keywords in text_keywords]



text_splitter = CustomTextSplitter("\n\n",10)

# 加载文档并分割
loader = UnstructuredLoader("./电商产品数据.txt")
documents = loader.load()
chunks = text_splitter.split_documents(documents)

for chunk in chunks:
    print("chunk",chunk.page_content)



