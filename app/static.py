from fastapi import APIRouter, Request, HTTPException
from fastapi.responses import FileResponse
from os import path

static_router = APIRouter()

# serve built frontend from git submodule 
@static_router.get("/{full_path:path}", include_in_schema=False)
async def serve_my_app(request: Request, full_path: str):
    resources_path = "web/dist"
    filename = path.join(resources_path, full_path)
    index_path = path.join(resources_path, "index.html")

    if not path.isfile(index_path):
        raise HTTPException(status_code=404, detail="Item not found")

    if path.isfile(filename):
        return FileResponse(path=filename)
    
    return FileResponse(path=index_path)
