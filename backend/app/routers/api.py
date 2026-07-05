from fastapi import APIRouter
from app.routers import activity, health, voice

api_router = APIRouter(prefix="/api/v1")

api_router.include_router(health.router)
api_router.include_router(activity.router)
api_router.include_router(voice.router)
