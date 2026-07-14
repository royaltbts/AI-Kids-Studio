"""
Lesson Agent

Generates the lesson plan and stores it in the EpisodeContext.
"""

import json

from backend.app.providers.provider_factory import ProviderFactory
from backend.app.schemas.episode_context import EpisodeContext
from backend.app.schemas.lesson import LessonResponse
from backend.app.services.prompt_service import PromptService


class LessonAgent:
    """
    Generates a lesson and updates the EpisodeContext.
    """

    def __init__(self):
        self.provider = ProviderFactory.get_provider()

    def generate(
        self,
        context: EpisodeContext,
    ) -> EpisodeContext:
        """
        Generate a lesson and attach it to the context.
        """

        prompt = PromptService.build_lesson_prompt(
            topic=context.topic,
            age_group=context.age_group,
        )

        response = self.provider.generate(prompt)

        lesson = LessonResponse(
            **json.loads(response)
        )

        context.lesson = lesson

        return context