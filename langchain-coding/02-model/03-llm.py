import os

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()

# 百炼千问模型更适合走 chat.completions 接口，因此这里使用 ChatOpenAI。
llm = ChatOpenAI(
    model="qwen-plus",
    temperature=0.9,
    api_key=os.getenv("ALI_API_KEY"),
    base_url=os.getenv("ALI_API_BASE_URL"),
    timeout=60,
)


prompt = "请用一句话解释量子力学"

response = llm.invoke(prompt)

print(response.content)
