
import json


class MockProvider:

    def generate(self, prompt: str) -> str:

        return json.dumps(
            {
                "lesson_title": "ABC Adventure",
                "learning_objective": "Teach ABC to children",
                "difficulty": "Easy",
                "estimated_duration": 120,
                "keywords": [
                    "ABC",
                    "Learning",
                    "Fun",
                ],
            }
        )

    def provider_name(self):

        return "Mock Provider"