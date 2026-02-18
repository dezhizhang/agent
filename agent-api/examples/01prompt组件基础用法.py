
from datetime import datetime
from langchain_core.prompts import (
    PromptTemplate,
    ChatPromptTemplate,
    HumanMessagePromptTemplate,
    MessagesPlaceholder
)


prompt = PromptTemplate.from_template("请讲一个关于{subject}的冷笑话")
print(prompt.format(subject="程序员"))

print("*" * 60)
#
# chat_prompt = ChatPromptTemplate.from_messages([
#     ("system","你是OpenAI开发的聊天机器人,请根据用户提问进行回复，当前的时间为:{now}"),
#     MessagesPlaceholder("chat_history"),
#     HumanMessagePromptTemplate.from_template("请讲一个关于{subject}的冷笑话")
# ])
#
#
# chat_value = chat_prompt.invoke({
#     "now":datetime.now(),
#     "subject":"程序员",
#     "chat_history":[]
# })
#
# print(chat_value)

chat_prompt = ChatPromptTemplate.from_messages([
    ("system","你是OpenAI开发的聊天机器人,请根据用户提问进行回复，当前的时间为:{now}"),
    MessagesPlaceholder("chat_history"),
    HumanMessagePromptTemplate.from_template("请讲一个关于{subject}的冷笑话")
])

chat_value = chat_prompt.invoke({
    "now":datetime.now(),
    "subject":"程序员",
    "chat_history":[]
})

print(chat_value)

