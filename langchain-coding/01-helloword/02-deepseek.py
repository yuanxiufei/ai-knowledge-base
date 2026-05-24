import os
import sys

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()
sys.stdout.reconfigure(encoding="utf-8")


llm = ChatOpenAI(
    model="deepseek-chat",
    temperature=0.9,
    api_key=os.getenv("DEEPSEEK_API_KEY"),
    base_url=os.getenv("DEEPSEEK_API_BASE_URL"),
    timeout=60,
)

response = llm.invoke("你是谁？")
print(response.content)
