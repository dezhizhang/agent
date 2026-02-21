import os

import dotenv
from openai import OpenAI
from langchain_community.chat_message_histories import FileChatMessageHistory

dotenv.load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),
    base_url=os.getenv("OPENAI_API_BASE"),
)

chat_history = FileChatMessageHistory("./memory.txt")


while True:
    query = input("Human:")

    if query == "q":
        exit(0)

    system_prompt = (
        "你是OpenAI开发的ChatGPT聊天机器人,可以根据相应的上下文回复用户信息，上下文里存放的是人类与你的对话信息"
        f"<context>{chat_history}</context>\n\n"
    )

    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role":"system","content":system_prompt},
            {"role":"user","content":query},
        ],
        stream=True
    )

    ai_content = ""
    for chunk in response:
        content = chunk.choices[0].delta.content
        if content is None:
            break
        ai_content += content
        print(content,flush=True,end="")
    chat_history.add_user_message(query)
    chat_history.add_ai_message(ai_content)


    print("")

