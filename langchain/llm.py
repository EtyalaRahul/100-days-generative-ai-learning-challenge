from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
import os

load_dotenv()

llm = ChatOpenAI(
    model="openai/gpt-4o",   # or any model available on AICredits
    api_key=os.getenv("OPENAI_API_KEY"),
    base_url="https://api.aicredits.in/v1",
    temperature=0
)

response = llm.invoke("Explain LangChain in simple words.")

print(response.content)