from fastapi import APIRouter

from backend.app.orchestrators.episode_orchestrator import EpisodeOrchestrator

router = APIRouter(
    prefix="/api/v1/lesson",
    tags=["Lesson"],
)

orchestrator = EpisodeOrchestrator()


@router.get("/generate")
def generate():

    return orchestrator.generate_episode(
        topic="ABC",
        age_group="3-5",
    )
