"""
Mock Voice Provider

Returns deterministic audio bytes for testing.
"""

from backend.app.voice_providers.base import VoiceProvider


class MockVoiceProvider(VoiceProvider):
    """
    Mock implementation of VoiceProvider.
    """

    def provider_name(self) -> str:
        """
        Return provider name.
        """

        return "mock"

    def generate_speech(
        self,
        text: str,
    ) -> bytes:
        """
        Return deterministic MP3 bytes.

        Parameters
        ----------
        text : str
            Ignored by the mock implementation.

        Returns
        -------
        bytes
            Dummy MP3 bytes.
        """

        return b"mock-mp3-data"
