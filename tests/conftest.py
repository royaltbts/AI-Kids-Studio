"""
Shared pytest fixtures.
"""

import pytest

from backend.app.providers.mock_provider import MockProvider
from backend.app.schemas.episode_context import EpisodeContext


@pytest.fixture
def mock_provider():
    return MockProvider()


@pytest.fixture
def sample_context():
    return EpisodeContext(
        topic="ABC",
        age_group="3-5",
    )
