"""
Tests for Media Pipeline.
"""

from backend.app.agents.image_prompt_agent import ImagePromptAgent
from backend.app.agents.lesson_agent import LessonAgent
from backend.app.agents.narration_agent import NarrationAgent
from backend.app.agents.scene_agent import SceneAgent
from backend.app.agents.story_agent import StoryAgent
from backend.app.schemas.episode_context import EpisodeContext
from backend.app.services.asset_assembler import AssetAssembler
from backend.app.services.media_pipeline import MediaPipeline


def test_media_pipeline():

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

    pipeline = MediaPipeline()

    images, audio = pipeline.render(
        assets,
    )

    assert len(images) == 4

    assert len(audio) == 4

    assert images[0].scene_number == 1

    assert audio[0].scene_number == 1

    assert images[3].scene_number == 4

    assert audio[3].scene_number == 4
