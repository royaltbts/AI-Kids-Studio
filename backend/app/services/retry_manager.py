"""
Retry Manager

Provides retry support with exponential backoff.
"""

from __future__ import annotations

import logging
import time
from collections.abc import Callable
from typing import ParamSpec, TypeVar

logger = logging.getLogger(__name__)

P = ParamSpec("P")
T = TypeVar("T")


class RetryManager:
    """
    Executes operations with retry support.
    """

    @staticmethod
    def run(
        func: Callable[P, T],
        *args: P.args,
        retries: int = 3,
        delay: float = 1.0,
        backoff: float = 2.0,
        retry_exceptions: tuple[type[Exception], ...] = (Exception,),
        **kwargs: P.kwargs,
    ) -> T:
        """
        Execute a callable using exponential backoff.
        """

        current_delay = delay

        for attempt in range(1, retries + 1):

            try:
                return func(*args, **kwargs)

            except retry_exceptions as error:

                if attempt == retries:
                    logger.exception(
                        "Retry limit reached after %s attempts.",
                        retries,
                    )
                    raise

                logger.warning(
                    ("Attempt %s/%s failed: %s. " "Retrying in %.1f seconds..."),
                    attempt,
                    retries,
                    error,
                    current_delay,
                )

                time.sleep(current_delay)

                current_delay *= backoff

        raise RuntimeError("Unexpected retry failure.")
