from fastapi import FastAPI

from .config.initial_config import load_env
from .routes import router

load_env()
app = FastAPI()
app.include_router(router)
