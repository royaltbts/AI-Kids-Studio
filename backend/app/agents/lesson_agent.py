"""
Lesson Agent

Generates lesson plans for TinyVerse episodes.
"""

from backend.app.agents.base_agent import BaseAgent
from backend.app.core.logger import logger
from backend.app.schemas.episode_context import EpisodeContext
from backend.app.schemas.lesson import LessonResponse
from backend.app.services.prompt_service import PromptService


class LessonAgent(BaseAgent):
    """
    Generates a lesson plan.
    """

    def __init__(
        self,
        provider: str | None = None,
    ) -> None:
        """
        Initialize the lesson agent.

        If a provider is supplied, it overrides the default provider.
        """

        super().__init__(provider)

    def generate(
        self,
        context: EpisodeContext,
    ) -> EpisodeContext:
        """
        Generate the lesson plan and store it in the context.
        """

        logger.info(
            "Generating lesson for topic '%s' using provider '%s'.",
            context.topic,
            self.provider.provider_name(),
        )

        prompt = PromptService.build_lesson_prompt(
            topic=context.topic,
            age_group=context.age_group,
        )

        context.lesson = self.generate_json(
            prompt=prompt,
            schema=LessonResponse,
        )

        logger.info("Lesson generated successfully.")

        return context
