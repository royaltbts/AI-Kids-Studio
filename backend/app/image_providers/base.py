"""
Base Image Provider

Abstract interface implemented by all image providers.
"""

from abc import ABC, abstractmethod


class ImageProvider(ABC):
    """
    Base interface for AI image providers.
    """

    @abstractmethod
    def provider_name(self) -> str:
        """
        Return the provider name.
        """
        raise NotImplementedError

    @abstractmethod
    def generate_image(
        self,
        prompt: str,
    ) -> bytes:
        """
        Generate an image.

        Parameters
        ----------
        prompt:
            Image generation prompt.

        Returns
        -------
        bytes
            Raw PNG image bytes.
        """
        raise NotImplementedError
