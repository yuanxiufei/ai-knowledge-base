import os

from dotenv import load_dotenv
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage
from langchain_openai import ChatOpenAI

# SystemMessage代表系统生成的消息或指令，通常用于指导AI的行为，比如设定AI的初始状态、行为模式或对话的总体目标。
# HumanMessage代表用户输入的消息或指令，比如问题、指令、命令等。
# AIMessage代表AI生成的消息。

load_dotenv()

llm = ChatOpenAI(
    model="deepseek-chat",
    temperature=0.9,
    api_key=os.getenv("DEEPSEEK_API_KEY"),
    base_url=os.getenv("DEEPSEEK_API_BASE_URL"),
    timeout=60,
)

messages = [
    SystemMessage(content="你是一个助手，请回答问题。"),
    HumanMessage(content="你好！"),
    AIMessage(content="你好，我是助手。"),
    HumanMessage(content="你叫什么名字？"),
]

response = llm.invoke(messages)
print("response type:", type(response).__name__)
print("response content:", response.content)
