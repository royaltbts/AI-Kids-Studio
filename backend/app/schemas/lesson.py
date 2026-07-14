from pydantic import BaseModel
from typing import List


class LessonResponse(BaseModel):

    lesson_title: str

    learning_objective: str

    difficulty: str

    estimated_duration: int

    keywords: List[str]