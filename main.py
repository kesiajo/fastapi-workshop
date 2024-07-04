from fastapi import FastAPI
from schema.dataclass import MovieBaseModel
from schema.enums import GenreEnum
from schema.models import MovieModel
from settings import initialize_db


initialize_db()
app = FastAPI()

movies_list = MovieModel.objects.all()


@app.get("/")
async def root():
    return {"message": "Movie Time"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


@app.get("/movies")
async def get_all_movies(offset: int = 1, limit: int = 50, genre: GenreEnum = None):
    query_params = {}
    if genre:
        query_params['genre'] = genre
    all_movies = MovieModel.objects(**query_params).skip(offset).limit(limit)
    return [MovieBaseModel(name=movie.name, genre=movie.genre, release_date=movie.release_date, rating=movie.rating, language=movie.language) for movie in all_movies]


@app.get("/movies/{name}")
async def get_movie(name: str):
    movie = movies_list.get(name=name)
    return MovieBaseModel(name=movie.name, genre=movie.genre, release_date=movie.release_date, rating=movie.rating, language=movie.language)


@app.post("/movies")
async def create_movie(movie: MovieBaseModel):
    MovieModel.objects.create(**movie.dict())
    return f"Successfully added {movie.name}"


@app.delete("/movies/{name}")
async def delete_movie(name: str):
    MovieModel.objects.get(name=name).delete()
    return f"Successfully deleted {name}"


@app.put("/movies/{name}")
async def update_movie(movie: MovieBaseModel):
    mobie = movies_list.get(name=movie.name)
    mobie.update(**movie.dict())
    return {"message": f"Successfully updated {movie.name}"}

