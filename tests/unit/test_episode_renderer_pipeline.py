"""
Tests for Episode Rendering Pipeline.
"""

from backend.app.agents.image_prompt_agent import ImagePromptAgent
from backend.app.agents.lesson_agent import LessonAgent
from backend.app.agents.narration_agent import NarrationAgent
from backend.app.agents.scene_agent import SceneAgent
from backend.app.agents.story_agent import StoryAgent
from backend.app.schemas.episode_context import EpisodeContext
from backend.app.services.asset_assembler import AssetAssembler
from backend.app.services.media_pipeline import MediaPipeline
from backend.app.video.video_factory import VideoFactory


def test_episode_renderer_pipeline():

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

    rendered_episode = MediaPipeline().render(
        assets,
    )

    renderer = VideoFactory.episode_renderer()

    video = renderer.render(
        rendered_episode,
    )

    assert video.title == "TinyVerse Episode"

    assert video.duration_seconds == 120

    assert video.video_path.endswith("episode.mp4")

    assert video.provider == "mock"

    assert video.status == "rendered"

    assert video.format == "mp4"

    assert video.fps == 30
