"""
Asset Assembler

Combines AI-generated outputs into renderable scene assets.
"""

import logging

logger = logging.getLogger(__name__)

from backend.app.schemas.episode_assets import EpisodeAssets
from backend.app.schemas.episode_context import EpisodeContext
from backend.app.schemas.scene_asset import SceneAsset


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

        scene_count = len(context.scene_plan.scenes)

        logger.info("Assembling episode assets.")

        for index in range(scene_count):
            asset = SceneAsset(
                scene=context.scene_plan.scenes[index],
                image_prompt=context.image_prompts[index],
                narration=context.narrations[index],
            )

            assets.scenes.append(asset)

        logger.info("Assembled %d scene assets.", len(assets.scenes))

        return assets
