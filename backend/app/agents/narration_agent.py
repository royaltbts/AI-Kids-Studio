"""
Narration Agent

Generates narration for every storyboard scene.
"""

import logging

from backend.app.agents.base_agent import BaseAgent
from backend.app.schemas.episode_context import EpisodeContext
from backend.app.schemas.narration import Narration
from backend.app.services.prompt_service import PromptService

logger = logging.getLogger(__name__)


class NarrationAgent(BaseAgent):
    """
    Generates narration for storyboard scenes.
    """

    def __init__(self):
        super().__init__()

    def generate(
        self,
        context: EpisodeContext,
    ) -> EpisodeContext:
        """
        Generate narration for every storyboard scene.
        """

        narrations: list[Narration] = []

        # If there's no scene_plan or scenes, nothing to generate.
        if not context.scene_plan or not getattr(context.scene_plan, "scenes", None):
            context.narrations = narrations
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

        logger.info("Generating narrations.")
        logger.info(
    "Generated %d narrations.",
    len(context.narrations),
)

        return context
