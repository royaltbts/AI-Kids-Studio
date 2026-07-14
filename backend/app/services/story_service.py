"""
Story Service

Responsible for generating educational stories.

This service communicates with the OpenAI service and
returns structured data back to the API layer.
"""

from backend.app.schemas.story import StoryResponse
from backend.app.services.openai_service import OpenAIService


class StoryService:

    def __init__(self):
        self.ai = OpenAIService()

    def generate_story(
        self,
        topic: str,
        age_group: str
    ) -> StoryResponse:

        story = self.ai.generate_story(
            topic=topic,
            age_group=age_group
        )

        return StoryResponse(
            title=f"{topic} Adventure",
            story=story,
            moral="Learning together makes every adventure fun!"
        )