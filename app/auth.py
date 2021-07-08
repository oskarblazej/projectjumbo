from fastapi import APIRouter, Response, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from jose import jwt, JWTError
from passlib.hash import bcrypt
from pydantic import BaseModel

from .config import config
from .db import users, todos

ALGORITHM = "HS256"
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/login")
auth_router = APIRouter()


class Credentials(BaseModel):
    name: str
    password: str


@auth_router.post("/login")
async def login(credentials: Credentials, response: Response):
    # users.getBy returns list of matching users
    user = users.getBy({"name": credentials.name})

    if len(user) == 0:
        response.status_code = 403
        return {"detail": "Bad username or password"}

    user = user[0]

    if not bcrypt.verify(credentials.password, user["password"]):
        response.status_code = 403
        return {"detail": "Bad username or password"}

    token = jwt.encode(
        {"name": user["name"], "id": user["id"]}, config["SECRET_KEY"], algorithm=ALGORITHM)

    return token


async def get_user(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, config["SECRET_KEY"], algorithms=ALGORITHM)

        return payload
    except JWTError:
        raise HTTPException(
            status_code=401,
            detail="Not authenticated"
        )
