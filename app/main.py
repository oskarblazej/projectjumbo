from fastapi import FastAPI, Depends

from .auth import auth_router
from .todos import todos_router

app = FastAPI()

app.include_router(auth_router)
app.include_router(todos_router)
