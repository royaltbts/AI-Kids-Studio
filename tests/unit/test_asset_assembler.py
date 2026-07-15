"""
Unit tests for AssetAssembler.
"""

from backend.app.agents.image_prompt_agent import ImagePromptAgent
from backend.app.agents.lesson_agent import LessonAgent
from backend.app.agents.narration_agent import NarrationAgent
from backend.app.agents.scene_agent import SceneAgent
from backend.app.agents.story_agent import StoryAgent
from backend.app.schemas.episode_context import EpisodeContext
from backend.app.services.asset_assembler import AssetAssembler


def test_build_episode_assets():

    context = EpisodeContext(
        topic="ABC",
        age_group="3-5",
    )

    context = LessonAgent().generate(context)
    context = StoryAgent().generate(context)
    context = SceneAgent().generate(context)
    context = ImagePromptAgent().generate(context)
    context = NarrationAgent().generate(context)

    assets = AssetAssembler.build(context)

    assert len(assets.scenes) == 4

    assert assets.scenes[0].scene.scene_number == 1
    assert assets.scenes[1].scene.scene_number == 2
    assert assets.scenes[2].scene.scene_number == 3
    assert assets.scenes[3].scene.scene_number == 4

    assert assets.scenes[0].image_prompt is not None
    assert assets.scenes[0].narration is not None

    assert assets.total_duration == 120
