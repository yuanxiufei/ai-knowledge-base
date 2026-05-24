import os
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI    
load_dotenv()

llm = ChatOpenAI(
    model="deepseek-chat",
    temperature=0.9,
    api_key=os.getenv("DEEPSEEK_API_KEY"),
    base_url=os.getenv("DEEPSEEK_API_BASE_URL"),
    timeout=60,
)

prompt_template = ChatPromptTemplate.from_messages([
    ("system", "你是个乐于助人的助手。"),
    ("user", "给我们讲一个有关{topic}的笑话。"),
])

prompt = prompt_template.invoke({"topic": "李世民"})
print("-----------------prompt-----------------")
print("prompt:", prompt)
print("-----------------prompt toJSON-----------------")
print("prompt toJSON:", prompt.to_json())
print("-----------------prompt toString-----------------")
print("prompt toString :", prompt.to_string())
print("-----------------prompt toMessages-----------------")
print("prompt toMessages:", prompt.to_messages())
print("-----------------prompt content-----------------")
print("prompt content:", prompt.to_messages()[-1].content)
