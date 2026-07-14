from fastapi import APIRouter

from backend.app.agents.lesson_agent import LessonAgent

router = APIRouter(
    prefix="/api/v1/lesson",
    tags=["Lesson"],
)

agent = LessonAgent()


@router.get("/generate")
def generate():

    return agent.generate(
        topic="ABC",
        age_group="3-5",
    )