"""
Tests for application settings.
"""

from backend.app.core.settings import settings


def test_settings():

    assert settings.PROJECT_NAME == "TinyVerse"

    assert settings.OUTPUT_DIR.name == "output"

    assert settings.IMAGE_DIR == "images"

    assert settings.AUDIO_DIR == "audio"

    assert settings.VIDEO_DIR == "video"

    assert settings.MUSIC_DIR == "music"

    assert settings.LOG_DIR == "logs"

    assert settings.DEFAULT_FPS == 30

    assert settings.DEFAULT_IMAGE_WIDTH == 1920

    assert settings.DEFAULT_IMAGE_HEIGHT == 1080
