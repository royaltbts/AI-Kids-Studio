"""
Unit tests for NarrationAgent.
"""

from backend.app.agents.image_prompt_agent import ImagePromptAgent
from backend.app.agents.lesson_agent import LessonAgent
from backend.app.agents.narration_agent import NarrationAgent
from backend.app.agents.scene_agent import SceneAgent
from backend.app.agents.story_agent import StoryAgent
from backend.app.schemas.episode_context import EpisodeContext


def test_generate_narrations():

    context = EpisodeContext(
        topic="ABC",
        age_group="3-5",
    )

    context = LessonAgent().generate(context)
    context = StoryAgent().generate(context)
    context = SceneAgent().generate(context)
    context = ImagePromptAgent().generate(context)
    context = NarrationAgent().generate(context)

    assert len(context.narrations) == 4

    assert context.narrations[0].scene_number == 1
    assert context.narrations[1].scene_number == 2
    assert context.narrations[2].scene_number == 3
    assert context.narrations[3].scene_number == 4

    for narration in context.narrations:
        assert narration.voice == "Friendly Female"
        assert narration.language == "English"
        assert narration.duration_seconds == 30
        assert narration.narration != ""
