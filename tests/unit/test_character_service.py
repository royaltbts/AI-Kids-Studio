"""
Unit tests for CharacterService.
"""

from backend.app.characters.character_service import CharacterService


def test_get_main_character():
    character = CharacterService.get_main_character()

    assert character.id == "toby"
    assert character.name == "Toby Bear"


def test_list_characters():
    characters = CharacterService.list_characters()

    assert len(characters) == 4


def test_get_character():
    character = CharacterService.get_character("leo")

    assert character.name == "Leo Lion"
