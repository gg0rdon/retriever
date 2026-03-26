import types
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
  return {"message": "Welcome to retriever, the happiest, cutes and friendliest issue tracker there is :) !"}
