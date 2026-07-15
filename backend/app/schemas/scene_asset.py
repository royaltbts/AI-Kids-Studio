"""
Scene Asset Schema

Represents every asset required to render one storyboard scene.
"""

from typing import Optional

from pydantic import BaseModel, Field

from backend.app.schemas.image_prompt import ImagePrompt
from backend.app.schemas.narration import Narration
from backend.app.schemas.scene import Scene


class SceneAsset(BaseModel):
    """
    Complete production asset for one storyboard scene.
    """

    # Original storyboard scene
    scene: Scene

    # AI-generated assets
    image_prompt: Optional[ImagePrompt] = None

    narration: Optional[Narration] = None

    # Future rendering assets
    background_music: str = ""

    sound_effects: list[str] = Field(default_factory=list)

    camera_direction: str = ""

    subtitle: str = ""

    animation_notes: str = ""
