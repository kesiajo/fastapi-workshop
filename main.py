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
async def get_all_movies():
    return list(movies_list.values())


@app.get("/movies/{name}")
async def get_movie(name: str):
    return movies_list[name]
