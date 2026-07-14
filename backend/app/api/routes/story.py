"""
Story API Routes

This module exposes endpoints related to story generation.

Future Features:
- Story
- Song
- Quiz
- Image Prompts
- Narration
"""

from fastapi import APIRouter, HTTPException

from backend.app.schemas.story import (
    StoryRequest,
    StoryResponse,
)

from backend.app.services.story_service import StoryService

router = APIRouter(
    prefix="/api/v1/story",
    tags=["Story"],
)

story_service = StoryService()


@router.post(
    "/generate",
    response_model=StoryResponse,
    summary="Generate Educational Story",
    description="Generates an educational story using AI.",
)
def generate_story(request: StoryRequest):

    try:

        return story_service.generate_story(
            topic=request.topic,
            age_group=request.age_group,
        )

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=f"Story generation failed: {str(e)}",
        )