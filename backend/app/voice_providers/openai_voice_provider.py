"""
OpenAI Voice Provider

Generates speech using the OpenAI Text-to-Speech API.
"""

from openai import OpenAI

from backend.app.core.settings import settings
from backend.app.voice_providers.base import VoiceProvider


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

    def generate_speech(
        self,
        text: str,
    ) -> bytes:
        """
        Generate speech from text.

        Parameters
        ----------
        text : str
            Text to synthesize.

        Returns
        -------
        bytes
            MP3 audio bytes.
        """

        response = self.client.audio.speech.create(
            model=settings.OPENAI_TTS_MODEL,
            voice=settings.OPENAI_TTS_VOICE,
            input=text,
            response_format="mp3",
        )

        return response.read()
