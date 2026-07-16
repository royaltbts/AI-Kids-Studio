"""
Narration Agent

Generates narration for storyboard scenes.
"""

import logging

from backend.app.agents.base_agent import BaseAgent
from backend.app.schemas.episode_context import EpisodeContext
from backend.app.schemas.narration import Narration
from backend.app.services.prompt_service import PromptService

logger = logging.getLogger(__name__)


class NarrationAgent(BaseAgent):
    """
    Generates narrations.
    """

    def __init__(
        self,
        provider: str | None = None,
    ) -> None:
        """
        Initialize the narration agent.

        If a provider is supplied, it overrides the default provider.
        """

        super().__init__(provider)

    def generate(
        self,
        context: EpisodeContext,
    ) -> EpisodeContext:
        """
        Generate narrations.
        """

        logger.info(
            "Generating narrations using provider '%s'.",
            self.provider.provider_name(),
        )

        narrations: list[Narration] = []

        if context.scene_plan is None:
            return context

        for scene in context.scene_plan.scenes:

            prompt = PromptService.build_narration_prompt(
                topic=context.topic,
                age_group=context.age_group,
                scene_number=scene.scene_number,
                scene_title=scene.title,
                narration=scene.narration,
            )

            narration = self.generate_json(
                prompt=prompt,
                schema=Narration,
            )

            narrations.append(narration)

        context.narrations = narrations

        logger.info(
            "Generated %d narrations.",
            len(context.narrations),
        )

        return context
