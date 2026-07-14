"""
Unit tests for SceneAgent.
"""

from backend.app.agents.lesson_agent import LessonAgent
from backend.app.agents.story_agent import StoryAgent
from backend.app.agents.scene_agent import SceneAgent
from backend.app.schemas.episode_context import EpisodeContext


def test_generate_scene_plan():

    context = EpisodeContext(
        topic="ABC",
        age_group="3-5",
    )

    context = LessonAgent().generate(context)
    context = StoryAgent().generate(context)
    context = SceneAgent().generate(context)

    assert context.scene_plan is not None
    assert len(context.scene_plan.scenes) == 4

    assert context.scene_plan.scenes[0].scene_number == 1
    assert context.scene_plan.scenes[0].title != ""
