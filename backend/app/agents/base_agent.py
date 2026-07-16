"""
Base Agent

Common functionality shared by all AI agents.
"""

import json
import re
from abc import ABC
from json import JSONDecodeError
from typing import TypeVar

from pydantic import BaseModel

from backend.app.providers.provider_factory import ProviderFactory

T = TypeVar("T", bound=BaseModel)


class BaseAgent(ABC):
    """
    Base class for all TinyVerse AI agents.
    """

    def __init__(
        self,
        provider: str | None = None,
    ) -> None:
        """
        Initialize the configured AI provider.

        If a provider name is supplied, it overrides the default
        provider configured in the application settings.
        """

        self.provider = ProviderFactory.get_provider(provider)

    @staticmethod
    def _extract_json(
        response: str,
    ) -> str:
        """
        Extract a JSON object from an LLM response.

        Supports:

        - Raw JSON
        - ```json ... ```
        - ``` ... ```
        - Explanatory text surrounding JSON
        """

        response = response.strip()

        # Already JSON
        if response.startswith("{") or response.startswith("["):
            return response

        # ```json ... ```
        fenced = re.search(
            r"```(?:json)?\s*(.*?)\s*```",
            response,
            flags=re.DOTALL | re.IGNORECASE,
        )

        if fenced:
            return fenced.group(1).strip()

        # Fallback: first JSON object
        start = response.find("{")
        end = response.rfind("}")

        if start != -1 and end != -1 and end > start:
            return response[start : end + 1]

        return response

    def generate_json(
        self,
        prompt: str,
        schema: type[T],
    ) -> T:
        """
        Generate structured JSON using the configured AI provider.
        """

        response = self.provider.generate(prompt)

        response = self._extract_json(response)

        try:
            data = json.loads(response)

        except JSONDecodeError as exc:
            raise ValueError(
                (
                    f"{self.provider.provider_name()} returned invalid JSON.\n\n"
                    f"Response:\n{response}"
                )
            ) from exc

        try:
            return schema.model_validate(data)

        except Exception as exc:
            raise ValueError(
                (
                    f"Response from '{self.provider.provider_name()}' "
                    f"does not match schema '{schema.__name__}'.\n\n"
                    f"Parsed Data:\n{json.dumps(data, indent=2)}"
                )
            ) from exc
