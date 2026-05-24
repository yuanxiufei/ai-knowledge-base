from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
load_dotenv()
# SystemMessage代表系统生成的消息或指令，通常用于指导AI的行为，比如设定AI的初始状态、行为模式或对话的总体目标。
# HumanMessage代表用户输入的消息或指令，比如问题、指令、命令等。
# AIMessage代表AI生成的消息。
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage