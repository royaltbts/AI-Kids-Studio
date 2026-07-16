"""
Unit tests for StoryAgent.
"""

from backend.app.agents.lesson_agent import LessonAgent
from backend.app.agents.story_agent import StoryAgent
from backend.app.schemas.episode_context import EpisodeContext


def test_generate_story():

    context = EpisodeContext(
        topic="ABC",
        age_group="3-5",
    )

    context = LessonAgent("mock").generate(context)
    context = StoryAgent("mock").generate(context)

    assert context.story is not None
    assert context.story.title == "ABC Adventure"
    assert len(context.story.scenes) == 4
