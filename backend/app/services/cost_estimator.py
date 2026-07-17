"""
Cost Estimator

Estimates the approximate cost of generating a TinyVerse episode.
"""

from __future__ import annotations

from backend.app.core.settings import settings


class CostEstimator:
    """
    Estimates generation cost using configurable pricing.
    """

    @staticmethod
    def estimate_image_cost(
        image_count: int,
    ) -> float:
        """
        Estimate image generation cost.
        """

        return round(
            image_count * settings.OPENAI_IMAGE_COST,
            4,
        )

    @staticmethod
    def estimate_tts_cost(
        character_count: int,
    ) -> float:
        """
        Estimate Text-to-Speech cost.

        Pricing is based on characters converted to
        thousands of characters.
        """

        return round(
            (character_count / 1000) * settings.OPENAI_TTS_COST_PER_1K,
            4,
        )

    @staticmethod
    def estimate_llm_cost(
        token_count: int,
    ) -> float:
        """
        Estimate LLM generation cost.

        Pricing is based on thousands of tokens.
        """

        return round(
            (token_count / 1000) * settings.OPENAI_LLM_COST_PER_1K,
            4,
        )

    @classmethod
    def estimate_total(
        cls,
        *,
        image_count: int,
        character_count: int,
        token_count: int,
    ) -> float:
        """
        Estimate total episode generation cost.
        """

        image_cost = cls.estimate_image_cost(
            image_count,
        )

        tts_cost = cls.estimate_tts_cost(
            character_count,
        )

        llm_cost = cls.estimate_llm_cost(
            token_count,
        )

        return round(
            image_cost + tts_cost + llm_cost,
            4,
        )
