"""
OpenAI Image Provider

Generates images using the OpenAI Images API.
"""

import base64
import logging

from openai import APIConnectionError, APITimeoutError, OpenAI, RateLimitError

from backend.app.core.settings import settings
from backend.app.image_providers.base import ImageProvider
from backend.app.services.retry_manager import RetryManager

logger = logging.getLogger(__name__)


class OpenAIImageProvider(ImageProvider):
    """
    OpenAI implementation of ImageProvider.
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
        prompt: str,
    ):
        """
        Execute a single OpenAI Images request.
        """

        return self.client.images.generate(
            model=settings.OPENAI_IMAGE_MODEL,
            prompt=prompt,
            size="1024x1024",
        )

    def generate_image(
        self,
        prompt: str,
    ) -> bytes:
        """
        Generate an image and return PNG bytes.
        """

        logger.info("Generating image using OpenAI.")

        response = RetryManager.run(
            self._generate,
            prompt,
            retries=settings.OPENAI_MAX_RETRIES,
            delay=settings.OPENAI_RETRY_DELAY,
            backoff=settings.OPENAI_RETRY_BACKOFF,
            retry_exceptions=(
                APITimeoutError,
                APIConnectionError,
                RateLimitError,
            ),
        )

        if not response.data:
            raise ValueError("OpenAI returned no image.")

        image_base64 = response.data[0].b64_json

        if image_base64 is None:
            raise ValueError("OpenAI returned empty image.")

        return base64.b64decode(image_base64)
