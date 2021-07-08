from fastapi import FastAPI, Response
from .db import users, todos
from passlib.hash import bcrypt
from pydantic import BaseModel
from jose import jwt

# openssl rand -hex 32
SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
ALGORITHM = "HS256"

app = FastAPI()

class Credentials(BaseModel):
    name: str
    password: str

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/login")
async def login(credentials: Credentials, response: Response):
    # users.getBy returns list of matching users
    user = users.getBy({"name": credentials.name})

    if len(user) == 0:
        response.status_code = 403
        return {"error": "bad username or password"}

    user = user[0]

    if not bcrypt.verify(credentials.password, user["password"]):
        response.status_code = 403
        return {"error": "bad username or password"}

    token = jwt.encode({"name": user["name"], "id": user["id"]}, SECRET_KEY, algorithm=ALGORITHM)

    return token