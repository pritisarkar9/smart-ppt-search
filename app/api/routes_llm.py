from fastapi import APIRouter
from pydantic import BaseModel
from app.core.groq_client import get_llm

router = APIRouter()

class Query(BaseModel):
    question:str

@router.post("/ask-llm")
def ask_llm(q:Query):
    llm = get_llm()
    response = llm.invoke(q.question)
    return {
        "question" : q.question,
        "ans": response.content
    }
