from abc import ABC, abstractmethod


class AIProvider(ABC):

    @abstractmethod
    def generate(self, prompt: str) -> str:
        """
        Generate text from a prompt.
        """
        pass

    @abstractmethod
    def provider_name(self) -> str:
        pass