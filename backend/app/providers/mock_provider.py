from backend.app.schemas.lesson import LessonResponse


class MockProvider:

    def generate_lesson(
        self,
        topic: str,
        age_group: str,
    ):

        return LessonResponse(

            lesson_title=f"{topic} Adventure",

            learning_objective=f"Teach {topic} to children",

            difficulty="Easy",

            estimated_duration=120,

            keywords=[
                topic,
                "Learning",
                "Fun",
            ],
        )

    def generate_story(
        self,
        topic: str,
        age_group: str,
    ):

        return f"Toby Bear learned about {topic} today."