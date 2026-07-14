"""
OpenAI Service

Responsible only for communicating with OpenAI.
"""

from openai import OpenAI

from backend.app.core.config import settings


class OpenAIService:

    def __init__(self):
        self.client = OpenAI(
            api_key=settings.OPENAI_API_KEY
        )

    def generate_story(
        self,
        topic: str,
        age_group: str,
    ) -> str:

        prompt = f"""
You are an expert children's educational storyteller.

Write an ORIGINAL story.

Topic:
{topic}

Age Group:
{age_group}

Characters:
- Toby Bear (Main Character)
- Mimi Rabbit
- Leo Lion
- Ellie Elephant

Rules:
- Simple English
- Happy tone
- Educational
- 250-350 words
- End with a positive moral
- No violence
- No scary content

Return ONLY the story.
"""

        response = self.client.responses.create(
            model="gpt-5.5",
            input=prompt,
        )

        return response.output_text