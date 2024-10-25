from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers.auth import auth_router
from routers.api import api_router
import uvicorn

app = FastAPI(
    title="Project Name",
    summary="This is a template for FastAPI with authentication logic using JWT",
    version="0.0.1",
)

origins = [
    "127.0.0.1:8000/docs"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth_router)
app.include_router(api_router)

if __name__ == "__main__":
    uvicorn.run(
        "main:app", 
        host="127.0.0.1", 
        port=8000, 
        reload=True
    )