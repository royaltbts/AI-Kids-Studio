"""
Provider Factory

Creates the configured AI provider.
"""

from backend.app.core.config import settings
from backend.app.providers.mock_provider import MockProvider
from backend.app.providers.base import AIProvider


class ProviderFactory:
    """
    Factory responsible for returning the configured AI provider.
    """

    @staticmethod
    def get_provider() -> AIProvider:
        """
        Return the configured AI provider.
        """

        provider = settings.AI_PROVIDER.lower()

        if provider == "mock":
            return MockProvider()

        # Future providers
        #
        # if provider == "claude":
        #     return ClaudeProvider()
        #
        # if provider == "gemini":
        #     return GeminiProvider()
        #
        # if provider == "openai":
        #     return OpenAIProvider()
        #
        # if provider == "ollama":
        #     return OllamaProvider()

        raise ValueError(
            f"Unsupported AI provider: {provider}"
        )