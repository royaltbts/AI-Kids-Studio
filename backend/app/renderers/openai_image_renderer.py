"""
OpenAI Image Renderer

Generates images using the OpenAI Images API.
Supports automatic asset caching.
"""

import base64
import logging
from pathlib import Path

from openai import OpenAI

from backend.app.core.settings import settings
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
        Initialize the OpenAI client.
        """

        self.client = OpenAI(
            api_key=settings.OPENAI_API_KEY,
        )

    def render(
        self,
        image_prompt: ImagePrompt,
        output_path: Path,
    ) -> RenderedImage:
        """
        Render an image using OpenAI.

        If the image already exists it is reused.
        """

        #
        # Cached image
        #

        if output_path.exists():

            logger.info(
                "Using cached image for scene %s.",
                image_prompt.scene_number,
            )

            return RenderedImage(
                scene_number=image_prompt.scene_number,
                image_path=str(output_path),
                width=1024,
                height=1024,
                status="cached",
            )

        #
        # Generate image
        #

        logger.info(
            "Generating image for scene %s using %s.",
            image_prompt.scene_number,
            settings.IMAGE_PROVIDER,
        )

        response = self.client.images.generate(
            model=settings.OPENAI_IMAGE_MODEL,
            prompt=image_prompt.prompt,
            size="1024x1024",
        )

        if not response.data:
            raise ValueError("OpenAI returned no image.")

        if not response.data[0].b64_json:
            raise ValueError("OpenAI returned empty image.")

        image_bytes = base64.b64decode(
            response.data[0].b64_json,
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
