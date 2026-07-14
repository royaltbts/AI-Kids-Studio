class ScriptService:

    def generate_story(self, topic: str):

        return {
            "topic": topic,
            "story": f"Once upon a time, there was a happy {topic} who loved learning."
        }