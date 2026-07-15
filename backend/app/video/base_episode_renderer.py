"""
Episode Renderer

Base interface for episode renderers.
"""

from abc import ABC
from abc import abstractmethod

from backend.app.schemas.rendered_episode import RenderedEpisode
from backend.app.schemas.rendered_video import RenderedVideo


class EpisodeRenderer(ABC):
    """
    Base interface for video rendering.
    """

    @abstractmethod
    def render(
        self,
        episode: RenderedEpisode,
    ) -> RenderedVideo:
        """
        Render a complete episode.
        """
        raise NotImplementedError
