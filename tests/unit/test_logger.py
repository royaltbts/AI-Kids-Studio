"""
Tests for TinyVerse logger.
"""

from backend.app.core.logger import LOGGER_NAME, logger


def test_logger():

    assert logger.name == LOGGER_NAME

    assert logger is not None
