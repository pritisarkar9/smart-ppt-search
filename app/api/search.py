# app/api/search.py
from fastapi import APIRouter, Query
from app.services.search_engine import search_pdf

router = APIRouter()

@router.get("/search")
def search(query: str = Query(..., min_length=1)):
    results = search_pdf(query)
    return {
        "query": query,
        "results": results
    }
