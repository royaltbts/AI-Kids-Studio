"""
Provider Factory

Creates the configured AI provider.
"""

from backend.app.core.settings import settings
from backend.app.providers.base import AIProvider
from backend.app.providers.mock_provider import MockProvider
from backend.app.providers.openai_provider import OpenAIProvider


class ProviderFactory:
    """
    Factory responsible for returning the configured AI provider.
    """

    @staticmethod
    def get_provider(
        provider_name: str | None = None,
    ) -> AIProvider:
        """
        Return the configured AI provider.

        If provider_name is supplied, it overrides the default
        provider configured in the application settings.
        """

        provider = (
            provider_name.lower() if provider_name else settings.AI_PROVIDER.lower()
        )

        if provider == "mock":
            return MockProvider()

        if provider == "openai":
            if not settings.OPENAI_API_KEY:
                raise ValueError(
                    "OPENAI_API_KEY is required when using the OpenAI provider."
                )

            return OpenAIProvider()

        raise ValueError(f"Unsupported AI provider: {provider}")
