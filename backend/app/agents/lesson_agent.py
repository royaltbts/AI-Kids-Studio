from backend.app.providers.provider_factory import ProviderFactory


class LessonAgent:

    def __init__(self):

        self.provider = ProviderFactory.get_provider()

    def generate(
        self,
        topic: str,
        age_group: str,
    ):

        return self.provider.generate_lesson(
            topic,
            age_group,
        )