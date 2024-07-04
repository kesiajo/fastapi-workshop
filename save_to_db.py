from data import movies_list
from schema.enums import LanguageEnum, GenreEnum
from schema.models import MovieModel
from settings import initialize_db

initialize_db()

movies = list(movies_list.values())
for movie in movies:
    movie["language"] = LanguageEnum[movie["language"]]
    movie["genre"] = GenreEnum[movie["genre"]]
    MovieModel(**movie).save()