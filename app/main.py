from fastapi import FastAPI, Depends
from .auth import auth_router

app = FastAPI()

app.include_router(auth_router)
