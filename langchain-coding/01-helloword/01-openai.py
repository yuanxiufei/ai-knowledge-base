import os

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()


llm = ChatOpenAI(
    model="gpt-4.1-mini",
    temperature=0.9,
    api_key=os.getenv("OPENAI_API_KEY"),
    base_url=os.getenv("OPENAI_API_BASE_URL"),
    timeout=60,
)

response = llm.invoke("你是谁？")
print(response.content)
