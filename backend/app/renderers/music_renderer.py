"""
Music Renderer

Base interface for music renderers.
"""

from abc import ABC
from abc import abstractmethod

from backend.app.schemas.rendered_music import RenderedMusic


class MusicRenderer(ABC):
    """
    Base interface for music rendering providers.
    """

    @abstractmethod
    def render(
        self,
        title: str,
        duration_seconds: int,
    ) -> RenderedMusic:
        """
        Render background music.
        """
        raise NotImplementedError
