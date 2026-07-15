"""
Rendered Image Schema

Represents one generated image.
"""

from pydantic import BaseModel


class RenderedImage(BaseModel):
    """
    Metadata describing a rendered image.
    """

    scene_number: int

    image_path: str

    width: int = 1920

    height: int = 1080

    status: str = "rendered"
