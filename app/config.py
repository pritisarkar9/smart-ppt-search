import os
from pydantic_settings import BaseSettings, SettingsConfigDict
from functools import lru_cache
from pathlib import Path

print(Path(".env").exists())
BASEDIR = Path(__file__).resolve().parent.parent.parent

class Setting(BaseSettings):
    model_config=SettingsConfigDict(env_file=BASEDIR/".env")
    GROQ_API_KEY: str
    MODEL_NAME: str = 'llama3-70b-8192'


@lru_cache
def get_settings():
    return Setting()