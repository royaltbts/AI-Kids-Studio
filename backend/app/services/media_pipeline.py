"""
Media Pipeline

Coordinates media rendering for an episode.
"""

import logging

from backend.app.renderers.renderer_factory import RendererFactory
from backend.app.schemas.episode_assets import EpisodeAssets
from backend.app.schemas.rendered_audio import RenderedAudio
from backend.app.schemas.rendered_episode import RenderedEpisode
from backend.app.schemas.rendered_image import RenderedImage
from backend.app.schemas.rendered_music import RenderedMusic

logger = logging.getLogger(__name__)


class MediaPipeline:
    """
    Renders all media assets for an episode.
    """

    def __init__(self):
        self.image_renderer = RendererFactory.image_renderer()
        self.voice_renderer = RendererFactory.voice_renderer()
        self.music_renderer = RendererFactory.music_renderer()

    def render(
        self,
        assets: EpisodeAssets,
    ) -> RenderedEpisode:
        """
        Render all media assets.
        """

        rendered_images: list[RenderedImage] = []
        rendered_audio: list[RenderedAudio] = []
        rendered_music: RenderedMusic | None = None

        # ----------------------------------------------------------
        # Render Images & Audio
        # ----------------------------------------------------------

        for scene in assets.scenes:

            if scene.image_prompt:
                rendered_images.append(
                    self.image_renderer.render(
                        scene.image_prompt,
                    )
                )

            if scene.narration:
                rendered_audio.append(
                    self.voice_renderer.render(
                        scene.narration,
                    )
                )

        # ----------------------------------------------------------
        # Render Background Music
        # ----------------------------------------------------------

        rendered_music = self.music_renderer.render(
            title="TinyVerse Background Music",
            duration_seconds=assets.total_duration,
        )

        logger.info("Rendering media assets.")

        logger.info(
    "Rendered %d images and %d audio tracks.",
    len(rendered_images),
    len(rendered_audio),
)

        # ----------------------------------------------------------
        # Build Episode
        # ----------------------------------------------------------

        return RenderedEpisode(
            images=rendered_images,
            audio=rendered_audio,
            music=rendered_music,
            total_duration=assets.total_duration,
        )
