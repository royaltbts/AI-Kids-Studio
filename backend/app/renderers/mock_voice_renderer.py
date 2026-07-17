"""
Mock Voice Renderer

Returns deterministic rendered audio objects for testing.
"""

from pathlib import Path

from backend.app.renderers.base_renderer import BaseRenderer
from backend.app.schemas.narration import Narration
from backend.app.schemas.rendered_audio import RenderedAudio


class MockVoiceRenderer(BaseRenderer):
    """
    Mock implementation of a voice renderer.
    """

    def render(
        self,
        narration: Narration,
        output_path: Path,
    ) -> RenderedAudio:
        """
        Simulate audio rendering.
        """

        output_path.parent.mkdir(
            parents=True,
            exist_ok=True,
        )

        #
        # Create a small placeholder file so downstream
        # components can work with a real path.
        #

        output_path.write_bytes(b"Mock audio")

        return RenderedAudio(
            scene_number=narration.scene_number,
            title=narration.title,
            narration=narration.narration,
            voice=narration.voice,
            duration_seconds=narration.duration_seconds,
            audio_path=str(output_path),
            sample_rate=24000,
            channels=2,
            format="mp3",
            provider="mock",
            status="rendered",
        )
