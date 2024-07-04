import datetime
from pydantic import BaseModel, Field
from schema.enums import GenreEnum, LanguageEnum


class MovieBaseModel(BaseModel):
    """Movie base model"""
    name: str = Field(..., description="The name of the movie", max_length=30, min_length=3)
    genre: GenreEnum
    release_date: datetime.date
    rating: int = Field(..., lte=10, gte=1, description="The rating of the movie")
    language: LanguageEnum
