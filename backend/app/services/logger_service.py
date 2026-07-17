"""
Logger Service

Centralized logging utilities for TinyVerse.
"""

from __future__ import annotations

import logging
from pathlib import Path


class LoggerService:
    """
    Provides standardized logging for TinyVerse.
    """

    _logger = logging.getLogger("tinyverse")

    @classmethod
    def configure(
        cls,
        log_level: int = logging.INFO,
        log_file: Path | None = None,
    ) -> None:
        """
        Configure the TinyVerse logger.

        Safe to call multiple times.
        """

        if cls._logger.handlers:
            return

        cls._logger.setLevel(log_level)

        formatter = logging.Formatter(
            fmt="%(asctime)s | %(levelname)-8s | %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S",
        )

        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)

        cls._logger.addHandler(console_handler)

        if log_file is not None:
            log_file.parent.mkdir(
                parents=True,
                exist_ok=True,
            )

            file_handler = logging.FileHandler(
                log_file,
                encoding="utf-8",
            )

            file_handler.setFormatter(formatter)

            cls._logger.addHandler(file_handler)

    @classmethod
    def info(
        cls,
        message: str,
    ) -> None:
        cls._logger.info(message)

    @classmethod
    def warning(
        cls,
        message: str,
    ) -> None:
        cls._logger.warning(message)

    @classmethod
    def error(
        cls,
        message: str,
    ) -> None:
        cls._logger.error(message)

    @classmethod
    def episode_started(
        cls,
        topic: str,
        age_group: str,
    ) -> None:
        cls.info(f"Episode started | Topic='{topic}' | Age='{age_group}'")

    @classmethod
    def stage_completed(
        cls,
        stage: str,
    ) -> None:
        cls.info(f"Stage completed | {stage}")

    @classmethod
    def asset_rendered(
        cls,
        asset_type: str,
        scene_number: int,
    ) -> None:
        cls.info(f"{asset_type} rendered | Scene {scene_number}")

    @classmethod
    def retry(
        cls,
        operation: str,
        attempt: int,
    ) -> None:
        cls.warning(f"Retry {attempt} | {operation}")

    @classmethod
    def episode_finished(
        cls,
        workspace: Path,
    ) -> None:
        cls.info(f"Episode finished | {workspace}")
