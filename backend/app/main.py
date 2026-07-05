from fastapi import FastAPI

from app.config import settings
from app.database import create_tables
from app.routers.api import api_router

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
)


@app.on_event("startup")
def startup():
    create_tables()


app.include_router(api_router)