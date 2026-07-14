"""
Narration Schema

Represents narration generated for one storyboard scene.
"""

from pydantic import BaseModel


class Narration(BaseModel):
    """
    Narration for a storyboard scene.
    """

    scene_number: int

    title: str

    narration: str

    voice: str = "Friendly Female"

    language: str = "English"

    duration_seconds: int = 30
