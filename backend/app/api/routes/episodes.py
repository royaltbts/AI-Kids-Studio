"""
Episode API Routes.

Endpoints for generating TinyVerse episodes.
"""

from fastapi import APIRouter, HTTPException

from backend.app.api.schemas.generate_request import GenerateEpisodeRequest
from backend.app.api.schemas.generate_response import GenerateEpisodeResponse
from backend.app.workflows.episode_workflow import EpisodeWorkflow

router = APIRouter(
    prefix="/episodes",
    tags=["Episodes"],
)


@router.post(
    "",
    response_model=GenerateEpisodeResponse,
)
def generate_episode(
    request: GenerateEpisodeRequest,
) -> GenerateEpisodeResponse:
    """
    Generate a complete TinyVerse episode.
    """

    try:
        workflow = EpisodeWorkflow()

        result = workflow.generate_episode(
            topic=request.topic,
            age_group=request.age_group,
        )

        return GenerateEpisodeResponse(
            success=result.success,
            workspace=str(result.workspace),
            metadata_path=str(result.metadata_path),
            message="Episode generated successfully.",
        )

    except Exception as exc:
        raise HTTPException(
            status_code=500,
            detail=str(exc),
        ) from exc
