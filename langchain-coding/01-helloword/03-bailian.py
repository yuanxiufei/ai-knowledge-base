import os
import sys

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

# 加载 .env
load_dotenv()

# Windows 控制台 UTF-8
sys.stdout.reconfigure(encoding="utf-8")

# 初始化模型
llm = ChatOpenAI(
    model="qwen-max",
    temperature=0.9,
    api_key=os.getenv("ALI_API_KEY"),
    base_url=os.getenv("ALI_API_BASE_URL"),
    timeout=60,
)

# 调用
response = llm.invoke("你是谁？")

# 输出
print(response.content)