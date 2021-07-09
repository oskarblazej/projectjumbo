from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware

from .auth import auth_router
from .todos import todos_router

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth_router)
app.include_router(todos_router)
