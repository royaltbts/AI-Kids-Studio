"""
Unit tests for LessonAgent.
"""

from backend.app.agents.lesson_agent import LessonAgent
from backend.app.schemas.episode_context import EpisodeContext


def test_generate_lesson():

    agent = LessonAgent()

    context = EpisodeContext(
        topic="ABC",
        age_group="3-5",
    )

    result = agent.generate(context)

    assert result.lesson is not None
    assert result.lesson.lesson_title == "ABC Adventure"
    assert result.lesson.learning_objective != ""
