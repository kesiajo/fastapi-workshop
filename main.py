from fastapi import FastAPI
from data import movies_list
from schema.enums import GenreEnum

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


@app.get("/movies")
async def get_all_movies(offset: int, limit: int = 5, genre: GenreEnum = None):
    all_movies = list(movies_list.values())
    if genre is not None:
        all_movies = [movie for movie in all_movies if movie["genre"] == genre.value]
    movies_count = len(all_movies)
    start_index = (offset - 1) * limit
    end_index = start_index + limit
    if start_index >= movies_count:
        # ERROR
        return None
    return all_movies[start_index:end_index]


@app.get("/movies/{name}")
async def get_movie(name: str):
    return movies_list[name]


@app.get("/movies/genre/{genre}")
async def get_all_genre_movies(genre: GenreEnum):
    all_movies = list(movies_list.values())
    return [movie for movie in all_movies if movie["genre"] == genre.value]
