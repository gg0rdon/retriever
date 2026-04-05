from fastapi import FastAPI
from src.routes import issue_router, comment_router

app = FastAPI(
  title="Retriever Issue tracker.",
  description="This is my little issue tracker and tribute to my dog which I love A LOT.",
  version="1.0.0"
)

@app.get("/")
def read_root():
  return {"message": "Welcome to retriever, the happiest, cutes and friendliest issue tracker there is :) !"}

app.include_router(issue_router)
app.include_router(comment_router)