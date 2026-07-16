"""
Voice Provider

Abstract interface implemented by all text-to-speech providers.
"""

from abc import ABC, abstractmethod


class VoiceProvider(ABC):
    """
    Base interface for voice providers.
    """

    @abstractmethod
    def provider_name(self) -> str:
        """
        Return the provider name.
        """
        raise NotImplementedError

    @abstractmethod
    def generate_speech(
        self,
        text: str,
    ) -> bytes:
        """
        Convert text into speech.

        Parameters
        ----------
        text : str
            Text to synthesize.

        Returns
        -------
        bytes
            MP3 audio bytes.
        """
        raise NotImplementedError
