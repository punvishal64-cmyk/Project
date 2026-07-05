from fastapi import APIRouter

from app.config import settings
from app.models.health import HealthResponse

router = APIRouter()


@router.get("/", response_model=HealthResponse)
def health_check():
    return HealthResponse(
        status="running",
        message=settings.APP_NAME,
    )

