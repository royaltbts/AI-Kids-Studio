"""
Media Pipeline

Coordinates rendering of images, narration, music and scene videos.
"""

from pathlib import Path

from backend.app.core.settings import settings
from backend.app.renderers.renderer_factory import RendererFactory
from backend.app.schemas.episode_assets import EpisodeAssets
from backend.app.schemas.rendered_audio import RenderedAudio
from backend.app.schemas.rendered_episode import RenderedEpisode
from backend.app.schemas.rendered_image import RenderedImage
from backend.app.schemas.rendered_video import RenderedVideo


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
        self.video_renderer = RendererFactory.video_renderer()

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
        rendered_videos: list[RenderedVideo] = []

        for scene_asset in assets.scenes:

            #
            # Validate required assets
            #

            if scene_asset.image_prompt is None:
                raise ValueError(
                    f"Missing image prompt for scene "
                    f"{scene_asset.scene.scene_number}"
                )

            if scene_asset.narration is None:
                raise ValueError(
                    f"Missing narration for scene " f"{scene_asset.scene.scene_number}"
                )

            #
            # Build output paths
            #

            image_output_path = (
                workspace
                / settings.IMAGE_DIR
                / f"scene_{scene_asset.scene.scene_number:03d}.png"
            )

            audio_output_path = (
                workspace
                / settings.AUDIO_DIR
                / f"scene_{scene_asset.scene.scene_number:03d}.mp3"
            )

            video_output_path = (
                workspace
                / settings.VIDEO_DIR
                / f"scene_{scene_asset.scene.scene_number:03d}.mp4"
            )

            #
            # Render image
            #

            image = self.image_renderer.render(
                image_prompt=scene_asset.image_prompt,
                output_path=image_output_path,
            )

            rendered_images.append(image)

            #
            # Render narration
            #

            audio = self.voice_renderer.render(
                narration=scene_asset.narration,
                output_path=audio_output_path,
            )

            rendered_audio.append(audio)

            #
            # Render scene video
            #

            video = self.video_renderer.render(
                scene_number=scene_asset.scene.scene_number,
                title=scene_asset.scene.title,
                image_path=image_output_path,
                audio_path=audio_output_path,
                output_path=video_output_path,
            )

            rendered_videos.append(video)

        #
        # Render background music
        #

        rendered_music = self.music_renderer.render(
            title=assets.title or "TinyVerse Background Music",
            duration_seconds=assets.total_duration,
        )

        #
        # Build episode
        #

        return RenderedEpisode(
            images=rendered_images,
            audio=rendered_audio,
            videos=rendered_videos,
            music=rendered_music,
            total_duration=assets.total_duration,
            episode_title=assets.title,
            status="rendered",
        )
