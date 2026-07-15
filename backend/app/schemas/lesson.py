from typing import List

from pydantic import BaseModel


class LessonResponse(BaseModel):

    lesson_title: str

    learning_objective: str

    difficulty: str

    estimated_duration: int

    keywords: List[str]
