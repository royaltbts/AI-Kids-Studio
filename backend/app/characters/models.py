"""
Character Models

Defines reusable characters used throughout TinyVerse.
"""

from pydantic import BaseModel


class Character(BaseModel):
    """
    Represents a recurring TinyVerse character.
    """

    id: str

    name: str

    species: str

    age: int

    personality: str

    appearance: str

    clothing: str

    voice_style: str

    catch_phrase: str

    favorite_color: str

    image_prompt: str

    animation_notes: str
