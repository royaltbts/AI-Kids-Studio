"""
OpenAI Provider

Implementation of the OpenAI LLM provider.
"""

import logging

from openai import OpenAI

from backend.app.core.settings import settings
from backend.app.providers.base import AIProvider

logger = logging.getLogger(__name__)


class OpenAIProvider(AIProvider):
    """
    OpenAI implementation of AIProvider.
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

    def generate(
        self,
        prompt: str,
    ) -> str:
        """
        Generate a completion using OpenAI.
        """

        logger.info(
            "Sending prompt to OpenAI (%s).",
            settings.OPENAI_MODEL,
        )

        response = self.client.responses.create(
            model=settings.OPENAI_MODEL,
            input=prompt,
        )

        logger.info("Received response from OpenAI.")

        return response.output_text
