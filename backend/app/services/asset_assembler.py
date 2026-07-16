"""
Asset Assembler

Combines AI-generated outputs into renderable scene assets.
"""

import logging

from backend.app.schemas.episode_assets import EpisodeAssets
from backend.app.schemas.episode_context import EpisodeContext
from backend.app.schemas.scene_asset import SceneAsset

logger = logging.getLogger(__name__)


class AssetAssembler:
    """
    Builds EpisodeAssets from the generated episode context.
    """

    @staticmethod
    def build(
        context: EpisodeContext,
    ) -> EpisodeAssets:
        """
        Assemble renderable assets for every scene.
        """

        assets = EpisodeAssets(
            total_duration=(
                context.scene_plan.total_duration if context.scene_plan else 0
            ),
        )

        if not context.scene_plan:
            return assets

        logger.info("Assembling episode assets.")

        for scene, image_prompt, narration in zip(
            context.scene_plan.scenes,
            context.image_prompts,
            context.narrations,
            strict=True,
        ):
            assets.scenes.append(
                SceneAsset(
                    scene=scene,
                    image_prompt=image_prompt,
                    narration=narration,
                )
            )

        logger.info(
            "Assembled %d scene assets.",
            len(assets.scenes),
        )

        return assets
