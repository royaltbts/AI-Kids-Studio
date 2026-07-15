from fastapi import APIRouter

from backend.app.services.prompt_service import PromptService

router = APIRouter(
    prefix="/api/v1/prompt",
    tags=["Prompt"],
)


@router.get("/story")
def preview_story_prompt():

    return {
        "prompt": PromptService.build_story_prompt(
            topic="ABC",
            age_group="3-5",
        )
    }
