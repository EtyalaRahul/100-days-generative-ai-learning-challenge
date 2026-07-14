import os 
from dotenv import load_dotenv
from langchain_ollama import OllamaLLM
import streamlit as st
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser


load_dotenv() 

##Langsmith tracking
# st.title("krish naik course")
os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"]="true"
os.environ["LANGCHAIN_PROJECT"]=os.getenv("LANGCHAIN_PROJECT")

##Prompt Template
prompt=ChatPromptTemplate.from_messages(
  [
    ("system","You are a helpful assistant please respond to the question asked"),
    ("user","Question: {question}")
  ]
)

##Streamlit framework
st.title("Langchain Demo with gemma2b")
input_text=st.text_input("what question do you want to ask?")

##Ollama  gemma2b model 
llm=OllamaLLM(model="gemma:2b") 
output_parser=StrOutputParser()
chain=prompt | llm | output_parser 

if input_text :
  st.write(chain.invoke({"question" : input_text})) 

