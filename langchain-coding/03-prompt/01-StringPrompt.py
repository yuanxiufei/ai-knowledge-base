import os

from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI

# 从 .env 中加载 DeepSeek 的 Key 和 Base URL。
load_dotenv()

llm = ChatOpenAI(
    model="deepseek-chat",
    temperature=0.9,
    api_key=os.getenv("DEEPSEEK_API_KEY"),
    base_url=os.getenv("DEEPSEEK_API_BASE_URL"),
    timeout=60,
)

# String Prompt: 先定义一个带变量占位符的字符串模板。
prompt_template = PromptTemplate.from_template("给我讲一个关于{topic}的笑话。")

# 把 topic 填入模板，得到最终发送给模型的提示词文本。
prompt = prompt_template.invoke({"topic": "李小龙"})


# 将渲染后的 prompt 发给聊天模型，并打印回复内容。
response = llm.invoke(prompt)
print(response.content)

