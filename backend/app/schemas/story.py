from typing import List

from pydantic import BaseModel, Field


class StoryRequest(BaseModel):
    topic: str = Field(..., description="Learning topic")
    age_group: str = Field(default="3-5")


class EpisodeInfo(BaseModel):
    title: str
    learning_objective: str
    age_group: str


class Character(BaseModel):
    name: str
    role: str


class Scene(BaseModel):
    scene_number: int
    narration: str
    image_prompt: str
    duration: int


class Song(BaseModel):
    title: str
    lyrics: str


class QuizQuestion(BaseModel):
    question: str
    options: List[str]
    answer: str


class StoryResponse(BaseModel):
    episode: EpisodeInfo
    characters: List[Character]
    scenes: List[Scene]
    song: Song
    quiz: List[QuizQuestion]
    moral: str
