"""
Unit tests for MediaPipeline.
"""

from backend.app.agents.image_prompt_agent import ImagePromptAgent
from backend.app.agents.lesson_agent import LessonAgent
from backend.app.agents.narration_agent import NarrationAgent
from backend.app.agents.scene_agent import SceneAgent
from backend.app.agents.story_agent import StoryAgent
from backend.app.schemas.episode_context import EpisodeContext
from backend.app.services.asset_assembler import AssetAssembler
from backend.app.services.media_pipeline import MediaPipeline
from backend.app.storage.output_manager import OutputManager


def test_media_pipeline():
    """
    Verify the complete media rendering pipeline.
    """

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

    workspace = OutputManager.create_episode_workspace()

    rendered = MediaPipeline().render(
        workspace=workspace,
        assets=assets,
    )

    assert len(rendered.images) == 4
    assert len(rendered.audio) == 4
    assert rendered.music is not None
    assert rendered.total_duration > 0
