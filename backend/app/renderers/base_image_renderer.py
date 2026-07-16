"""
Base Image Renderer

Base interface for image rendering.
"""

from abc import abstractmethod

from backend.app.renderers.base_renderer import BaseRenderer
from backend.app.schemas.image_prompt import ImagePrompt
from backend.app.schemas.rendered_image import RenderedImage


class ImageRenderer(BaseRenderer):
    """
    Base class for image renderers.
    """

    @abstractmethod
    def render(
        self,
        image_prompt: ImagePrompt,
    ) -> RenderedImage:
        """
        Render one image.
        """
        raise NotImplementedError
