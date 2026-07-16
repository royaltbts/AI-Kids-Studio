"""
OpenAI Image Provider

Generates images using the OpenAI Images API.
"""

import base64

from openai import OpenAI

from backend.app.core.settings import settings
from backend.app.image_providers.base import ImageProvider


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

    def generate_image(
        self,
        prompt: str,
    ) -> bytes:
        """
        Generate an image and return PNG bytes.
        """

        response = self.client.images.generate(
            model="gpt-image-1",
            prompt=prompt,
            size="1024x1024",
        )

        image_base64 = response.data[0].b64_json

        return base64.b64decode(image_base64)
