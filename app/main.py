# app/main.py
from fastapi import FastAPI
from app.api.routes_llm import router as llm_router

app = FastAPI(title="Smart PPT Search")

app.include_router(llm_router,prefix="/api")


@app.get("/")
def health_check():
    return {"status": "running"}
