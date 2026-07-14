"""
Character Registry

Central registry for all TinyVerse characters.
"""

from backend.app.characters.default_characters import (
    TOBY,
    MIMI,
    LEO,
    ELLIE,
)
from backend.app.characters.models import Character

CHARACTERS: dict[str, Character] = {
    TOBY.id: TOBY,
    MIMI.id: MIMI,
    LEO.id: LEO,
    ELLIE.id: ELLIE,
}
