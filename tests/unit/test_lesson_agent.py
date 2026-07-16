"""
Unit tests for LessonAgent.
"""

from backend.app.agents.lesson_agent import LessonAgent
from backend.app.schemas.episode_context import EpisodeContext


def test_generate_lesson():
    """
    Verify lesson generation using the mock provider.
    """

    agent = LessonAgent("mock")

    context = EpisodeContext(
        topic="ABC",
        age_group="3-5",
        provider="mock",
    )

    result = agent.generate(context)

    assert result.lesson is not None
    assert result.lesson.lesson_title == "ABC Adventure"
    assert (
        result.lesson.learning_objective == "Teach children to recognize the letter A."
    )
    assert result.lesson.difficulty == "Easy"
    assert result.lesson.estimated_duration == 120
    assert "Alphabet" in result.lesson.keywords
