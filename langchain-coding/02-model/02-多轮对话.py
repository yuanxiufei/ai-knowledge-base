import os
import sys

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

# SystemMessage代表系统生成的消息或指令，通常用于指导AI的行为，比如设定AI的初始状态、行为模式或对话的总体目标。
# HumanMessage代表用户输入的消息或指令，比如问题、指令、命令等。
# AIMessage代表AI生成的消息。
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
load_dotenv()
sys.stdout.reconfigure(encoding="utf-8")




llm = ChatOpenAI(
    model="deepseek-chat",
    temperature=0.9,
    api_key=os.getenv("DEEPSEEK_API_KEY"),
    base_url=os.getenv("DEEPSEEK_API_BASE_URL"),
    timeout=60,
)

messages = [
    SystemMessage(content="你是历史专家，请用中文回答。"),
    HumanMessage(content="我的身份是皇帝，名字叫李世民"),
    AIMessage(content="你好，我是皇帝李世民"),
    HumanMessage(content="玄武门事件是什么事件？"),
    AIMessage(content="玄武门事件是一个历史事件。"),
    HumanMessage(content="玄武门事件发生的时间是时候？"),
]

response = llm.invoke(messages)
print(response.content)
