from abc import ABC, abstractmethod


class AIProvider(ABC):

    @abstractmethod
    def generate_lesson(
        self,
        topic: str,
        age_group: str,
    ):
        pass

    @abstractmethod
    def generate_story(
        self,
        topic: str,
        age_group: str,
    ):
        pass