"""
OpenAI Service

Handles communication with the OpenAI API.
"""

from openai import OpenAI

from backend.app.core.config import settings
from backend.app.services.prompt_service import PromptService


class OpenAIService:
    """
    Service responsible for communicating with OpenAI.
    """

    def __init__(self):
        self.client = OpenAI(
            api_key=settings.OPENAI_API_KEY
        )

    def generate_story(
        self,
        topic: str,
        age_group: str,
    ) -> str:
        """
        Generate a story using OpenAI.
        """

        prompt = PromptService.build_story_prompt(
            topic=topic,
            age_group=age_group,
        )

        response = self.client.responses.create(
            model="gpt-5.5",
            input=prompt,
        )

        return response.output_text