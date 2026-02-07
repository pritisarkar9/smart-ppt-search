# app/main.py
from fastapi import FastAPI
from app.api.search import router as search_router

app = FastAPI(title="Smart PPT Search")

app.include_router(search_router, prefix="/api")

@app.get("/")
def health_check():
    return {"status": "running"}
