"""
Character Service

Provides helper methods for accessing TinyVerse characters.
"""

from backend.app.characters.models import Character
from backend.app.characters.registry import CHARACTERS


class CharacterService:
    """
    Service for retrieving characters.
    """

    @staticmethod
    def get_character(character_id: str) -> Character:
        """
        Return a character by ID.
        """

        if character_id not in CHARACTERS:
            raise ValueError(
                f"Unknown character: {character_id}"
            )

        return CHARACTERS[character_id]

    @staticmethod
    def list_characters() -> list[Character]:
        """
        Return all registered characters.
        """

        return list(CHARACTERS.values())

    @staticmethod
    def get_main_character() -> Character:
        """
        Return TinyVerse's main character.
        """

        return CHARACTERS["toby"]