from fastapi import FastAPI 
from langchain_core.prompts import ChatPromptTemplate 
from langchain_core.output_parsers import StrOutputParser 
from langchain_groq import ChatGroq 
import os 
from dotenv import load_dotenv
from langserve import add_routes
load_dotenv() 


groq_api_key=os.getenv('GROQ_API_KEY')

llm=ChatGroq(
  model="llama-3.1-8b-instant",
  groq_api_key=groq_api_key
) 


##1. Create Prompt template
System_template="Translate the following into {Language}: "
prompt_template=ChatPromptTemplate.from_messages([
  ('system',System_template),
  ('user','{text}')
]) 

parser=StrOutputParser() 

##create chain 
chain=prompt_template | llm | parser


##App defination 

app=FastAPI(title="Langchain server",version="1.0",description="A simple API server using Langchain runnable interfaces")

## Adding chain routes
add_routes(
  app,
  chain,
  path="/chain"
) 

if __name__=='__main__' :
  import uvicorn 
  uvicorn.run(app,host="localhost",port=8000)