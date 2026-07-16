"""
Media Pipeline

Coordinates rendering of images, narration, music and video.
"""

from pathlib import Path

from backend.app.core.settings import settings
from backend.app.renderers.renderer_factory import RendererFactory
from backend.app.schemas.episode_assets import EpisodeAssets
from backend.app.schemas.rendered_audio import RenderedAudio
from backend.app.schemas.rendered_episode import RenderedEpisode
from backend.app.schemas.rendered_image import RenderedImage
from backend.app.schemas.rendered_music import RenderedMusic


class MediaPipeline:
    """
    Coordinates rendering of all episode media.
    """

    def __init__(self) -> None:
        """
        Initialize configured renderers.
        """

        self.image_renderer = RendererFactory.image_renderer()
        self.voice_renderer = RendererFactory.voice_renderer()
        self.music_renderer = RendererFactory.music_renderer()

    def render(
        self,
        workspace: Path,
        assets: EpisodeAssets,
    ) -> RenderedEpisode:
        """
        Render all media assets into the episode workspace.
        """

        rendered_images: list[RenderedImage] = []
        rendered_audio: list[RenderedAudio] = []

        #
        # Render Images
        #

        for scene_asset in assets.scenes:

            if scene_asset.image_prompt:

                output_path = (
                    workspace
                    / settings.IMAGE_DIR
                    / f"scene_{scene_asset.scene.scene_number:03d}.png"
                )

                rendered_images.append(
                    self.image_renderer.render(
                        image_prompt=scene_asset.image_prompt,
                        output_path=output_path,
                    )
                )

            #
            # Render Narration
            #

            if scene_asset.narration:

                rendered_audio.append(
                    self.voice_renderer.render(
                        scene_asset.narration,
                    )
                )

        #
        # Render Background Music
        #

        rendered_music: RenderedMusic = self.music_renderer.render(
            title=assets.title or "TinyVerse Background Music",
            duration_seconds=assets.total_duration,
        )

        #
        # Assemble Episode
        #

        return RenderedEpisode(
            images=rendered_images,
            audio=rendered_audio,
            music=rendered_music,
            total_duration=assets.total_duration,
            episode_title=assets.title,
            status="rendered",
        )
