"""
Mock Image Provider

Returns deterministic image bytes for testing.
"""

from backend.app.image_providers.base import ImageProvider


class MockImageProvider(ImageProvider):
    """
    Mock implementation of ImageProvider.
    """

    def provider_name(self) -> str:
        """
        Return provider name.
        """

        return "mock"

    def generate_image(
        self,
        prompt: str,
    ) -> bytes:
        """
        Return deterministic image bytes.

        Parameters
        ----------
        prompt:
            Ignored by the mock implementation.

        Returns
        -------
        bytes
            Dummy PNG bytes.
        """

        return b"mock-image-data"