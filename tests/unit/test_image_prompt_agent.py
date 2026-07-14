"""
Unit tests for ImagePromptAgent.
"""

from backend.app.agents.image_prompt_agent import ImagePromptAgent
from backend.app.agents.lesson_agent import LessonAgent
from backend.app.agents.scene_agent import SceneAgent
from backend.app.agents.story_agent import StoryAgent
from backend.app.schemas.episode_context import EpisodeContext


def test_generate_image_prompts():

    context = EpisodeContext(
        topic="ABC",
        age_group="3-5",
    )

    context = LessonAgent().generate(context)
    context = StoryAgent().generate(context)
    context = SceneAgent().generate(context)
    context = ImagePromptAgent().generate(context)

    assert len(context.image_prompts) == 4

    assert context.image_prompts[0].scene_number == 1
    assert context.image_prompts[1].scene_number == 2
    assert context.image_prompts[2].scene_number == 3
    assert context.image_prompts[3].scene_number == 4

    assert context.image_prompts[0].title.lower() == "meet toby"
    assert context.image_prompts[1].title.lower() == "the letter a"
    assert context.image_prompts[2].title.lower() == "learning together"
    assert context.image_prompts[3].title.lower() == "celebrate learning"

    for prompt in context.image_prompts:
        assert prompt.style == "Pixar 3D"
        assert prompt.aspect_ratio == "16:9"
        assert prompt.prompt != ""
