"""
TinyVerse Logger

Centralized logging configuration.
"""

import logging

LOGGER_NAME = "tinyverse"

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
)

logger = logging.getLogger(LOGGER_NAME)
