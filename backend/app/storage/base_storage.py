"""
Base Storage Interface.
"""

from abc import ABC, abstractmethod
from pathlib import Path


class BaseStorage(ABC):
    """
    Abstract storage backend.
    """

    @abstractmethod
    def save(
        self,
        relative_path: str,
        content: bytes,
    ) -> Path:
        """
        Save content and return the full path.
        """
        raise NotImplementedError

    @abstractmethod
    def exists(
        self,
        relative_path: str,
    ) -> bool:
        """
        Check if a file exists.
        """
        raise NotImplementedError
