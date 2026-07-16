"""
Image Prompt Agent

Generates image prompts for every storyboard scene.
"""

import logging

from backend.app.agents.base_agent import BaseAgent
from backend.app.schemas.episode_context import EpisodeContext
from backend.app.schemas.image_prompt import ImagePrompt
from backend.app.services.prompt_service import PromptService

logger = logging.getLogger(__name__)


class ImagePromptAgent(BaseAgent):
    """
    Generates image prompts for storyboard scenes.
    """

    def __init__(self):
        super().__init__()

    def generate(
        self,
        context: EpisodeContext,
    ) -> EpisodeContext:
        """
        Generate image prompts for all storyboard scenes.
        """

        image_prompts: list[ImagePrompt] = []

        if context.scene_plan is None:
            return context

        logger.info("Generating image prompts.")

        for scene in context.scene_plan.scenes:
            prompt = PromptService.build_image_prompt(
                topic=context.topic,
                age_group=context.age_group,
                scene_number=scene.scene_number,
                scene_title=scene.title,
                narration=scene.narration,
                visual_description=scene.visual_description,
                characters="Toby Bear",
            )

            image_prompt = self.generate_json(
                prompt=prompt,
                schema=ImagePrompt,
            )

            image_prompts.append(image_prompt)

        context.image_prompts = image_prompts

        logger.info(
            "Generated %d image prompts.",
            len(context.image_prompts),
        )

        return context
