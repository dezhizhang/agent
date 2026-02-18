from langchain_core.prompts import PromptTemplate

full_template = PromptTemplate.from_template(
"""
{instruction}
{example}
{start}
"""
)

instruction_prompt = PromptTemplate.from_template("你正在模拟 {person}")

example_prompt = PromptTemplate.from_template(
"Q:{example_q}\nA:{example_a}"
)

start_prompt = PromptTemplate.from_template(
"现在，请回答用户的问题:\nQ:{input}\nA:"
)

# 先格式化子模板
instruction = instruction_prompt.format(person="雷军")

example = example_prompt.format(
    example_q="你最喜欢的汽车？",
    example_a="我喜欢小米汽车"
)

start = start_prompt.format(input="你今年的目标是什么？")

# 再拼总模板
final_prompt = full_template.format(
    instruction=instruction,
    example=example,
    start=start
)

print(final_prompt)
