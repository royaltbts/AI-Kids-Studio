"""
OpenAI Voice Provider

Generates speech using the OpenAI Text-to-Speech API.
"""

import logging

from openai import APIConnectionError, APITimeoutError, OpenAI, RateLimitError

from backend.app.core.settings import settings
from backend.app.services.retry_manager import RetryManager
from backend.app.voice_providers.base import VoiceProvider

logger = logging.getLogger(__name__)


class OpenAIVoiceProvider(VoiceProvider):
    """
    OpenAI implementation of VoiceProvider.
    """

    def __init__(self) -> None:
        """
        Initialize the OpenAI client.
        """

        self.client = OpenAI(
            api_key=settings.OPENAI_API_KEY,
        )

    def provider_name(self) -> str:
        """
        Return provider name.
        """

        return "openai"

    def _generate(
        self,
        text: str,
    ):
        """
        Execute a single OpenAI TTS request.
        """

        return self.client.audio.speech.create(
            model=settings.OPENAI_TTS_MODEL,
            voice=settings.OPENAI_TTS_VOICE,
            input=text,
            response_format="mp3",
        )

    def generate_speech(
        self,
        text: str,
    ) -> bytes:
        """
        Generate speech from text and return MP3 bytes.
        """

        logger.info("Generating speech using OpenAI.")

        response = RetryManager.run(
            self._generate,
            text,
            retries=settings.OPENAI_MAX_RETRIES,
            delay=settings.OPENAI_RETRY_DELAY,
            backoff=settings.OPENAI_RETRY_BACKOFF,
            retry_exceptions=(
                APITimeoutError,
                APIConnectionError,
                RateLimitError,
            ),
        )

        return response.read()
