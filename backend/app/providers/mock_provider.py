import json


class MockProvider:

    def generate(self, prompt: str) -> str:

        if "story outline" in prompt.lower():

            return json.dumps(
                {
                    "title": "ABC Adventure",

                    "introduction": "Toby Bear finds a magical alphabet book.",

                    "moral": "Learning letters is fun.",

                    "scenes": [
                        "Meet Toby",
                        "Find the Letter A",
                        "Learn Together",
                        "Celebrate Success"
                    ]
                }
            )

        return json.dumps(
            {
                "lesson_title": "ABC Adventure",

                "learning_objective": "Teach ABC to children",

                "difficulty": "Easy",

                "estimated_duration": 120,

                "keywords": [
                    "ABC",
                    "Learning",
                    "Fun"
                ]
            }
        )

    def provider_name(self):

        return "Mock Provider"