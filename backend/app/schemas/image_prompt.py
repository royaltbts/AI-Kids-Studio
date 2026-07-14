"""
Image Prompt Schema

Represents an image generation prompt for a storyboard scene.
"""

from pydantic import BaseModel


class ImagePrompt(BaseModel):
    """
    Image generation instructions for one scene.
    """

    scene_number: int

    title: str

    prompt: str

    negative_prompt: str = ""

    style: str = "Pixar 3D"

    aspect_ratio: str = "16:9"
