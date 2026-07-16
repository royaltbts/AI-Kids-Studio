"""
OpenAI Image Renderer

Renders AI-generated images to disk using the configured image provider.
"""

import logging
from pathlib import Path

from backend.app.image_providers.provider_factory import ImageProviderFactory
from backend.app.renderers.base_image_renderer import ImageRenderer
from backend.app.schemas.image_prompt import ImagePrompt
from backend.app.schemas.rendered_image import RenderedImage

logger = logging.getLogger(__name__)


class OpenAIImageRenderer(ImageRenderer):
    """
    OpenAI implementation of the image renderer.
    """

    def __init__(self) -> None:
        """
        Initialize the configured image provider.
        """

        self.provider = ImageProviderFactory.get_provider("openai")

    def render(
        self,
        image_prompt: ImagePrompt,
        output_path: Path,
    ) -> RenderedImage:
        """
        Generate an image and save it to disk.
        """

        logger.info(
            "Generating image for scene %s using %s.",
            image_prompt.scene_number,
            self.provider.provider_name(),
        )

        image_bytes = self.provider.generate_image(
            image_prompt.prompt,
        )

        output_path.parent.mkdir(
            parents=True,
            exist_ok=True,
        )

        output_path.write_bytes(image_bytes)

        logger.info(
            "Saved image to %s",
            output_path,
        )

        return RenderedImage(
            scene_number=image_prompt.scene_number,
            image_path=str(output_path),
            width=1024,
            height=1024,
            status="rendered",
        )
