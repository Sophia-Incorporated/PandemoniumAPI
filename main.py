import logging
import sys
from contextlib import asynccontextmanager

import uvicorn
from fastapi import FastAPI

from api.v1.routers.user_router import router as user_router
from config import settings
from database import sessionmanager

@asynccontextmanager
async def lifespan(app: FastAPI):
    yield
    if sessionmanager._engine is not None:
        await sessionmanager.close()

app = FastAPI(lifespan=lifespan, title=settings.project_name, docs_url="/api/v1/docs")

@app.get("/")
async def root():
    return { "message" : "Hello!"}

app.include_router(user_router)

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", reload=True, port=8000)