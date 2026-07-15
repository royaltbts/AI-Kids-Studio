"""
Asset Assembler

Combines AI-generated outputs into renderable scene assets.
"""

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
            total_duration=context.scene_plan.total_duration,
        )

        scene_count = len(context.scene_plan.scenes)

        for index in range(scene_count):

            asset = SceneAsset(
                scene=context.scene_plan.scenes[index],
                image_prompt=context.image_prompts[index],
                narration=context.narrations[index],
            )

            assets.scenes.append(asset)

        return assets
