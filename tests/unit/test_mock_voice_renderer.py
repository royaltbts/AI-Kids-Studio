"""
Tests for Mock Voice Renderer.
"""

from backend.app.renderers.mock_voice_renderer import MockVoiceRenderer
from backend.app.schemas.narration import Narration


def test_render_voice():

    narration = Narration(
        scene_number=1,
        title="Meet Toby",
        narration="Welcome to the forest!",
        voice="Friendly Female",
        language="English",
        duration_seconds=30,
    )

    rendered = MockVoiceRenderer().render(narration)

    assert rendered.scene_number == 1

    assert rendered.voice == "Friendly Female"

    assert rendered.duration_seconds == 30

    assert rendered.provider == "mock"

    assert rendered.status == "rendered"

    assert rendered.audio_path.endswith(
        "scene_001.mp3"
    )