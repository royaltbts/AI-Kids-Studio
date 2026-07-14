
import json

from backend.app.providers.provider_factory import ProviderFactory
from backend.app.schemas.lesson import LessonResponse
from backend.app.services.prompt_service import PromptService


class LessonAgent:

    def __init__(self):

        self.provider = ProviderFactory.get_provider()

    def generate(
        self,
        topic: str,
        age_group: str,
    ) -> LessonResponse:

        prompt = PromptService.build_lesson_prompt(
            topic,
            age_group,
        )

        response = self.provider.generate(prompt)

        data = json.loads(response)

        return LessonResponse(**data)