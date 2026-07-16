"""
Scene Agent

Generates storyboard scenes for a TinyVerse episode.
"""

import logging

from backend.app.agents.base_agent import BaseAgent
from backend.app.schemas.episode_context import EpisodeContext
from backend.app.schemas.scene_plan import ScenePlan
from backend.app.services.prompt_service import PromptService

logger = logging.getLogger(__name__)


class SceneAgent(BaseAgent):
    """
    Generates storyboard scenes.
    """

    def __init__(
        self,
        provider: str | None = None,
    ) -> None:
        """
        Initialize the scene agent.

        If a provider is supplied, it overrides the default provider.
        """

        super().__init__(provider)

    def generate(
        self,
        context: EpisodeContext,
    ) -> EpisodeContext:
        """
        Generate storyboard scenes.
        """

        logger.info(
            "Generating scene plan using provider '%s'.",
            self.provider.provider_name(),
        )

        prompt = PromptService.build_scene_agent_prompt(
            topic=context.topic,
            age_group=context.age_group,
            story_title=(context.story.title if context.story else ""),
            story_intro=(context.story.introduction if context.story else ""),
        )

        context.scene_plan = self.generate_json(
            prompt=prompt,
            schema=ScenePlan,
        )

        logger.info(
            "Generated %d scenes.",
            len(context.scene_plan.scenes),
        )

        return context
