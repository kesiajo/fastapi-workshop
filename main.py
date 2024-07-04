from fastapi import FastAPI
from data import movies_list

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


@app.get("/movies")
async def get_all_movies(offset: int, limit: int = 5):
    all_movies = list(movies_list.values())
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
