"""
Base Renderer

Abstract base class for all renderers.
"""

from abc import ABC, abstractmethod


class BaseRenderer(ABC):
    """
    Base interface for all renderers.
    """

    @abstractmethod
    def render(self, *args, **kwargs):
        """
        Render an asset.
        """
        raise NotImplementedError
