"""
Base Agent

Common functionality shared by all AI agents.
"""

import json
from abc import ABC
from typing import TypeVar

from pydantic import BaseModel

from backend.app.providers.provider_factory import ProviderFactory

T = TypeVar("T", bound=BaseModel)


class BaseAgent(ABC):
    """
    Base class for all TinyVerse AI agents.
    """

    def __init__(self):
        self.provider = ProviderFactory.get_provider()

    def generate_json(
        self,
        prompt: str,
        schema: type[T],
    ) -> T:
        """
        Generate structured JSON using the configured provider.
        """

        response = self.provider.generate(prompt)

        data = json.loads(response)

        return schema(**data)
