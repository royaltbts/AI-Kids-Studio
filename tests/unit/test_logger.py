"""
Tests for TinyVerse logger.
"""

from backend.app.core.logger import LOGGER_NAME
from backend.app.core.logger import logger


def test_logger():

    assert logger.name == LOGGER_NAME

    assert logger is not None
