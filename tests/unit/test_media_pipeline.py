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
    """
    Verify the complete media rendering pipeline.
    """

    context = EpisodeContext(
        topic="ABC",
        age_group="3-5",
    )

    # Generate episode content
    context = LessonAgent().generate(context)
    context = StoryAgent().generate(context)
    context = SceneAgent().generate(context)
    context = ImagePromptAgent().generate(context)
    context = NarrationAgent().generate(context)

    # Assemble renderable assets
    assets = AssetAssembler.build(context)

    # Render media
    pipeline = MediaPipeline()
    rendered = pipeline.render(assets)

    # ----------------------------------------------------------
    # Episode level validation
    # ----------------------------------------------------------

    assert rendered.total_duration == 120
    assert rendered.status == "rendered"

    # ----------------------------------------------------------
    # Images
    # ----------------------------------------------------------

    assert len(rendered.images) == 4

    assert rendered.images[0].scene_number == 1
    assert rendered.images[1].scene_number == 2
    assert rendered.images[2].scene_number == 3
    assert rendered.images[3].scene_number == 4

    assert rendered.images[0].image_path.endswith("scene_001.png")

    assert rendered.images[3].image_path.endswith("scene_004.png")

    assert rendered.images[0].width == 1920
    assert rendered.images[0].height == 1080
    assert rendered.images[0].status == "rendered"

    # ----------------------------------------------------------
    # Audio
    # ----------------------------------------------------------

    assert len(rendered.audio) == 4

    assert rendered.audio[0].scene_number == 1
    assert rendered.audio[1].scene_number == 2
    assert rendered.audio[2].scene_number == 3
    assert rendered.audio[3].scene_number == 4

    assert rendered.audio[0].audio_path.endswith("scene_001.mp3")

    assert rendered.audio[3].audio_path.endswith("scene_004.mp3")

    assert rendered.audio[0].voice == "Friendly Female"
    assert rendered.audio[0].status == "rendered"
    assert rendered.audio[0].format == "mp3"

    # ----------------------------------------------------------
    # Music
    # ----------------------------------------------------------

    assert rendered.music is not None
    assert rendered.music.title == "TinyVerse Background Music"

    assert rendered.music.duration_seconds == 120

    assert rendered.music.provider == "mock"

    assert rendered.music.status == "rendered"

    assert rendered.music.music_path.endswith("background.mp3")
