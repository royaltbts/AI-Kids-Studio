"""
Image Provider Factory

Creates configured image providers.
"""

from backend.app.core.settings import settings
from backend.app.image_providers.base import ImageProvider
from backend.app.image_providers.mock_image_provider import MockImageProvider
from backend.app.image_providers.openai_image_provider import OpenAIImageProvider


class ImageProviderFactory:
    """
    Factory responsible for creating image providers.
    """

    @staticmethod
    def get_provider(
        provider_name: str | None = None,
    ) -> ImageProvider:
        """
        Return the configured image provider.
        """

        provider = (
            provider_name.lower() if provider_name else settings.IMAGE_PROVIDER.lower()
        )

        if provider == "mock":
            return MockImageProvider()

        if provider == "openai":
            if not settings.OPENAI_API_KEY:
                raise ValueError(
                    "OPENAI_API_KEY is required when using the OpenAI image provider."
                )

            return OpenAIImageProvider()

        raise ValueError(f"Unsupported image provider: {provider}")
