
from langchain_text_splitters import TextSplitter
from typing import Any
import re

text = """
前言

这是本书的前言部分,介绍了写作背景和目的。

第1章介绍
1.1什么是人工智能
人工智能是研究如何使计算机能够像人一样思考和学习的学科抖

1.2人工智能的历史
人工智能的发展经历了多个阶段,从早期的符号主义到现代的深度学习。

第2章机器学习基础
2.1监督学习
监督学习是指从标记数据中学习预测模型的方法。

2.2无监督学习
无监督学习是指从无标记数据中发现模式的方法。
"""


class ChapterTextSplitter(TextSplitter):
    """基于章节标题的文本分割器,将文档按照章节结构分割"""

    def __init__(self, chapter_patterns: list[str] = None, keep_separator: bool = True, **kwargs: Any):
        super().__init__(**kwargs)

        if chapter_patterns is None:
            chapter_patterns = [
                r"第[一二三四五六七八九十百千万\d]+[章节卷部篇](?:\s+[^\n]+)?",
                r"[一二三四五六七八九十百千万\d]+\,\s+[^\n]+",
                r"(?:Chapter|Section)\s+[IVXivx\d]+(?:\.\s+[^\n]+)?",
                r"^(?:\d+\.)+\d+\s+[^\n]+"
            ]

        self.chapter_patterns = chapter_patterns
        self.keep_separator = keep_separator
        self.chapter_regexes = [re.compile(p, re.MULTILINE) for p in self.chapter_patterns]


    def split_text(self, text:str):
        """"""
        # 找到所有章节标题位置
        chapter_positions = []
        for regex in self.chapter_regexes:
            for match in regex.finditer(text):
                start,end = match.span()
                chapter_positions.append((start,end,match.group(0)))


        # 按位置排序
        chapter_positions.sort(key=lambda x:x[0])

        chunks = []
        if chapter_positions and chapter_positions[0][0] > 0:
            chunks.append(text[:chapter_positions[0][0]])


        # 添加所有章节
        for i in range(len(chapter_positions)):
            start, end, chapter = chapter_positions[i]
            next_start = chapter_positions[i+1][0] if  i + 1 < len(chapter_positions) else len(text)

            chunk_start = start if self.keep_separator else end
            chunks.append(text[chunk_start:next_start])

        return chunks



text_splitter = ChapterTextSplitter()
chunks = text_splitter.split_text(text)

for idx,chunk in enumerate(chunks):
    print(f"====块{idx + 1}======")
    print(chunk)



