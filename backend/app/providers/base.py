"""
Base AI Provider Interface
"""

from abc import ABC, abstractmethod


class AIProvider(ABC):
    """
    Abstract interface for every AI provider.
    """

    @abstractmethod
    def generate(self, prompt: str) -> str:
        """
        Generate a response from a prompt.
        """
        pass

    @abstractmethod
    def provider_name(self) -> str:
        """
        Return the provider name.
        """
        pass