"""
Media Pipeline

Coordinates media rendering for an episode.
"""

from backend.app.renderers.renderer_factory import RendererFactory
from backend.app.schemas.episode_assets import EpisodeAssets
from backend.app.schemas.rendered_audio import RenderedAudio
from backend.app.schemas.rendered_episode import RenderedEpisode
from backend.app.schemas.rendered_image import RenderedImage


class MediaPipeline:
    """
    Renders all media assets for an episode.
    """

    def __init__(self):

        self.image_renderer = RendererFactory.image_renderer()
        self.voice_renderer = RendererFactory.voice_renderer()

    def render(
        self,
        assets: EpisodeAssets,
    ) -> RenderedEpisode:
        """
        Render all images and narration.
        """

        rendered_images: list[RenderedImage] = []
        rendered_audio: list[RenderedAudio] = []

        for scene in assets.scenes:

            rendered_images.append(
                self.image_renderer.render(
                    scene.image_prompt,
                )
            )

            rendered_audio.append(
                self.voice_renderer.render(
                    scene.narration,
                )
            )

        return RenderedEpisode(
    images=rendered_images,
    audio=rendered_audio,
    total_duration=assets.total_duration,
)