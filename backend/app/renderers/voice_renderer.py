"""
Voice Renderer

Base interface for all voice renderers.
"""

from abc import ABC, abstractmethod

from backend.app.schemas.narration import Narration
from backend.app.schemas.rendered_audio import RenderedAudio


class VoiceRenderer(ABC):
    """
    Base interface for voice rendering providers.
    """

    @abstractmethod
    def render(
        self,
        narration: Narration,
    ) -> RenderedAudio:
        """
        Render narration into an audio file.
        """
        raise NotImplementedError