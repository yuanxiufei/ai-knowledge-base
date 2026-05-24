import os

from dotenv import load_dotenv
from langchain_openai import OpenAI

load_dotenv()

# 这个文件保留 OpenAI 的调用方式，用来记录“OpenAI Compatible / 文本补全风格”写法。
# 这里以阿里云百炼为例，方便对照 OpenAI 类的初始化方式。
# 如果实际接入的是 qwen-max、deepseek-chat、deepseek-reasoner 这类聊天模型，
# 更推荐改用 ChatOpenAI。
llm = OpenAI(
    model="qwen-plus",
    temperature=0.9,
    api_key=os.getenv("ALI_API_KEY"),
    base_url=os.getenv("ALI_API_BASE_URL"),
    timeout=60,
)


prompt = "请用一句话解释量子力学"

response = llm.invoke(prompt)

print(response)
