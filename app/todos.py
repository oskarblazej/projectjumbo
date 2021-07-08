from fastapi import APIRouter, Depends
from pydantic import BaseModel

from .auth import get_user
from .db import todos

todos_router = APIRouter()


class Todo(BaseModel):
    content: str
    done: bool


@todos_router.get("/todo")
async def get_todos(user: set = Depends(get_user)):
    return todos.getBy({"user": user["id"]})


@todos_router.post("/todo")
async def add_todo(todo: Todo, user: set = Depends(get_user)):
    todos.add({
        "user": user["id"],
        "content": todo.content,
        "done": todo.done,
    })


@todos_router.put("/todo/{todo_id}")
async def update_todo(todo_id: int, todo: Todo, user: set = Depends(get_user)):
    # TODO: check if todo belongs to user
    todos.updateById(todo_id, dict(todo))


@todos_router.delete("/todo/{todo_id}")
async def delete_todo(todo_id: int, user: set = Depends(get_user)):
    # TODO: check if todo belongs to user
    todos.deleteById(todo_id)
