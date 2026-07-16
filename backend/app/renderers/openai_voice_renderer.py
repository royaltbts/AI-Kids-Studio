"""
OpenAI Voice Renderer

Renders speech audio using the configured voice provider.
"""

import logging
from pathlib import Path

from backend.app.renderers.base_renderer import BaseRenderer
from backend.app.schemas.narration import Narration
from backend.app.schemas.rendered_audio import RenderedAudio
from backend.app.voice_providers.provider_factory import VoiceProviderFactory

logger = logging.getLogger(__name__)


class OpenAIVoiceRenderer(BaseRenderer):
    """
    OpenAI implementation of the voice renderer.
    """

    def __init__(self) -> None:
        """
        Initialize the configured voice provider.
        """

        self.provider = VoiceProviderFactory.get_provider("openai")

    def render(
        self,
        narration: Narration,
        output_path: Path,
    ) -> RenderedAudio:
        """
        Generate speech and save it as an MP3.
        """

        logger.info(
            "Generating narration for scene %s using %s.",
            narration.scene_number,
            self.provider.provider_name(),
        )

        audio_bytes = self.provider.generate_speech(
            narration.narration,
        )

        output_path.parent.mkdir(
            parents=True,
            exist_ok=True,
        )

        output_path.write_bytes(audio_bytes)

        logger.info(
            "Saved narration to %s",
            output_path,
        )

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
            provider=self.provider.provider_name(),
            status="rendered",
        )
