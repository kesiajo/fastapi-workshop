from fastapi import FastAPI, HTTPException, status
from data import movies_list
from schema.dataclass import MovieBaseModel
from schema.enums import GenreEnum

app = FastAPI()

movies_list = movies_list


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


@app.get("/movies")
async def get_all_movies(offset: int, limit: int = 50, genre: GenreEnum = None):
    all_movies = list(movies_list.values())
    if genre is not None:
        all_movies = [movie for movie in all_movies if movie["genre"] == genre.value]
    movies_count = len(all_movies)
    start_index = (offset - 1) * limit
    end_index = start_index + limit
    if start_index >= movies_count:
        raise HTTPException(status_code=status.INVALID_ARGUMENT, detail="Offset/limit is invalid")
    return all_movies[start_index:end_index]


@app.get("/movies/{name}")
async def get_movie(name: str):
    return movies_list[name]


@app.post("/movies")
async def create_movie(movie: MovieBaseModel):
    if movie.name in movies_list:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=f"Name {movie.name} already exists")
    movies_list[movie.name] = movie.dict()
    return f"Successfully added {movie.name}"


@app.delete("/movies/{name}")
async def delete_movie(name: str):
    if name not in movies_list:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Name {name} does not exists")
    del movies_list[name]
    return f"Successfully deleted {name}"


@app.put("/movies/{name}")
async def update_movie(movie: MovieBaseModel):
    movies_list[movie.name] = movie.dict()
    return {"message": f"Successfully updated {movie.name}"}

