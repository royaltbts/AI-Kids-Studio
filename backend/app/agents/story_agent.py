"""
Story Agent

Generates a structured story plan and stores it in the EpisodeContext.
"""

import json

from backend.app.providers.provider_factory import ProviderFactory
from backend.app.schemas.episode_context import EpisodeContext
from backend.app.schemas.story_plan import StoryPlan
from backend.app.services.prompt_service import PromptService


class StoryAgent:
    """
    Generates a StoryPlan and updates the EpisodeContext.
    """

    def __init__(self):
        self.provider = ProviderFactory.get_provider()

    def generate(
        self,
        context: EpisodeContext,
    ) -> EpisodeContext:
        """
        Generate a story plan and attach it to the context.
        """

        if context.lesson is None:
            raise ValueError(
                "Lesson must be generated before StoryAgent runs."
            )

        prompt = PromptService.build_story_agent_prompt(
            topic=context.topic,
            age_group=context.age_group,
            lesson_title=context.lesson.lesson_title,
            learning_objective=context.lesson.learning_objective,
        )

        response = self.provider.generate(prompt)

        story = StoryPlan(
            **json.loads(response)
        )

        context.story = story

        return context