from fastapi import APIRouter

from backend.app.core.settings import settings

router = APIRouter(prefix="/api/v1/system", tags=["System"])


@router.get("/info")
def system_info():
    return {
        "application": settings.APP_NAME,
        "version": settings.APP_VERSION,
        "status": "running",
    }
