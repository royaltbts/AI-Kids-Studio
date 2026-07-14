from fastapi import APIRouter
from backend.app.services.script_service import ScriptService

router = APIRouter()

service = ScriptService()


@router.get("/generate-story")
def generate_story(topic: str):
    return service.generate_story(topic)