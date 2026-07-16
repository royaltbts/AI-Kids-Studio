"""
Voice Provider Factory

Creates configured voice providers.
"""

from backend.app.core.settings import settings
from backend.app.voice_providers.base import VoiceProvider
from backend.app.voice_providers.mock_voice_provider import MockVoiceProvider
from backend.app.voice_providers.openai_voice_provider import OpenAIVoiceProvider


class VoiceProviderFactory:
    """
    Factory responsible for creating voice providers.
    """

    @staticmethod
    def get_provider(
        provider_name: str | None = None,
    ) -> VoiceProvider:
        """
        Return the configured voice provider.
        """

        provider = (
            provider_name.lower() if provider_name else settings.VOICE_PROVIDER.lower()
        )

        if provider == "mock":
            return MockVoiceProvider()

        if provider == "openai":
            if not settings.OPENAI_API_KEY:
                raise ValueError(
                    "OPENAI_API_KEY is required when using the OpenAI voice provider."
                )

            return OpenAIVoiceProvider()

        raise ValueError(f"Unsupported voice provider: {provider}")
