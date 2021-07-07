from fastapi import FastAPI
from .db import users, todos

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}