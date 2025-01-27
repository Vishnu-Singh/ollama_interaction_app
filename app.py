from fastapi import FastAPI
import uvicorn
from chat_engine import chat

app = FastAPI()

@app.get("/")
def index():
    return "Welcome to Ollama demo"

@app.get("/chat/{query}")
def index(query:str):
    response = chat(query)
    return response


if __name__ == "__main__":
    uvicorn.run(host="0.0.0.0",port=9000,app=app)