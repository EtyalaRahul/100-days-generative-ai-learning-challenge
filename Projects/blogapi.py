from fastapi import FastAPI 

app=FastAPI() 

@app.get('/app')
def hello_world() :
  return {
    "Hello" : "world"
  }

@app.get('/rahul') 
def rahul() :
  return "rahuletyala"