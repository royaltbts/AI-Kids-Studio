"""
Base Renderer

Abstract base class for all media renderers.
"""

from abc import ABC


class BaseRenderer(ABC):
    """
    Base class shared by all renderers.

    This class exists so every renderer has a common parent.
    Specialized renderer interfaces (ImageRenderer,
    VoiceRenderer, MusicRenderer) inherit from this class.
    """

    pass
