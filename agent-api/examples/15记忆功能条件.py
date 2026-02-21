import os
from typing import Any
import dotenv
from openai import OpenAI

dotenv.load_dotenv()


class ConversationSummaryBufferMemory:
    """摘要缓冲混合记忆类"""

    def __init__(self, summary: str = "", chat_histories: list = None, max_tokens: int = 300):
        self.summary = summary
        self.chat_histories = [] if chat_histories is None else chat_histories
        self.max_tokens = max_tokens
        self._client = OpenAI(
            api_key=os.getenv("OPENAI_API_KEY"),
            base_url=os.getenv("OPENAI_API_BASE"),
        )

    @classmethod
    def get_num_tokens(cls, query: str) -> int:
        """计算传入的query的token数"""
        return len(query)

    def save_context(self,human_query:str,ai_content:str) -> None:
        """保存传入的新一次对话信息"""
        self.chat_histories.append({"human":human_query,"ai":ai_content})

        buffer_string = self.get_buffer_string()

        tokens = self.get_num_tokens(buffer_string)

        if tokens > self.max_tokens:
            first_chat = self.chat_histories[0]
            self.summary = self.summary_text(
                self.summary,
                f"Human:{first_chat.get('human')}\nAI:{first_chat.get('ai')}"
            )
            del self.chat_histories[0]


    def get_buffer_string(self) -> str:
        """将历史对话转换成字符串"""
        buffer:str = ""
        for chat in self.chat_histories:
            buffer += f"Human:{chat.get('human')}\nAI:{chat.get('ai')}\n\n"
        return buffer.strip()


    def load_memory_variables(self) -> dict[str, Any]:
        """加载记忆变量为一个字典，便于格式化到prompt中"""
        buffer_string = self.get_buffer_string()
        return {
            "chat_history":f"摘要:{self.summary}\n\n历史信息：{buffer_string}\n"
        }


    def summary_text(self, origin_summary: str, new_line: str) -> str:
        """用于将旧摘要和传入的新对话生成一个新摘要"""
        prompt = f"""你是一个强大的聊天机器人, 请根据用户提供的谈话内容, 总结摘要, 并将其添加到先前提供的摘"""
        completion = self._client.chat.completions.create(
            model="gpt-4o",
            messages=[{"role":"user","content":prompt}]
        )

        return  completion.choices[0].message.content

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),
    base_url=os.getenv("OPENAI_API_BASE"),
)

memory = ConversationSummaryBufferMemory("", [], 300)

while True:
    query = input("Human:")

    if query == 'q':
        break

    memory_variables = memory.load_memory_variables()

    answer_prompt =(
        "你是一个强大的聊天机器人,请根据对应的上下文和用户提问解决问题。\n\n"
        f"{memory_variables.get('chat_histories')}\n\n"
        f"用户的提问题:{query}"
    )

    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "user", "content": answer_prompt}
        ],
        stream=True
    )

    # 循环读取流式响应内容
    ai_content = ""
    for chunk in response:
        content = chunk.choices[0].delta.content
        if content is None:
            break
        ai_content += content
    print("")
    memory.save_context(query,ai_content)
