"""
Mock Voice Renderer

Returns deterministic rendered audio objects for testing.
"""

from backend.app.renderers.voice_renderer import VoiceRenderer
from backend.app.schemas.narration import Narration
from backend.app.schemas.rendered_audio import RenderedAudio


class MockVoiceRenderer(VoiceRenderer):
    """
    Mock implementation of a voice renderer.
    """

    def render(
        self,
        narration: Narration,
    ) -> RenderedAudio:
        """
        Simulate audio rendering.
        """

        return RenderedAudio(
            scene_number=narration.scene_number,
            title=narration.title,
            narration=narration.narration,
            voice=narration.voice,
            duration_seconds=narration.duration_seconds,
            audio_path=(
                f"output/audio/"
                f"scene_{narration.scene_number:03d}.mp3"
            ),
            sample_rate=24000,
            channels=2,
            format="mp3",
            provider="mock",
            status="rendered",
        )