from langchain_groq import ChatGroq
from app.config import get_settings

settings = get_settings()

def get_llm():
    return ChatGroq(
        api_key = settings.GROQ_API_KEY,
        model= settings.MODEL_NAME,
        temperature=0.5   
    )