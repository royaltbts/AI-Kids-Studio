from backend.app.schemas.story import (
    Character,
    EpisodeInfo,
    QuizQuestion,
    Scene,
    Song,
    StoryResponse,
)


class StoryService:

    def generate_story(self, topic: str, age_group: str):

        return StoryResponse(
            episode=EpisodeInfo(
                title=f"{topic} Adventure",
                learning_objective=f"Learn about {topic}",
                age_group=age_group,
            ),
            characters=[
                Character(
                    name="Toby Bear",
                    role="Main Character",
                ),
                Character(
                    name="Mimi Rabbit",
                    role="Best Friend",
                ),
                Character(
                    name="Leo Lion",
                    role="Helper",
                ),
                Character(
                    name="Ellie Elephant",
                    role="Teacher",
                ),
            ],
            scenes=[
                Scene(
                    scene_number=1,
                    narration="Toby Bear discovers today's lesson.",
                    image_prompt="Cute teddy bear in colorful classroom",
                    duration=8,
                ),
                Scene(
                    scene_number=2,
                    narration="Friends learn together happily.",
                    image_prompt="Rabbit, Lion and Elephant smiling",
                    duration=8,
                ),
            ],
            song=Song(
                title="Learning Song",
                lyrics="A B C, let's learn happily...",
            ),
            quiz=[
                QuizQuestion(
                    question="What did Toby learn today?",
                    options=[
                        "ABC",
                        "Numbers",
                        "Colors",
                    ],
                    answer="ABC",
                )
            ],
            moral="Learning with friends is always fun!",
        )
