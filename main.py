from fastapi import FastAPI

from data.movies import movies

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


@app.get("/movies")
async def get_movies():
    return list(movies.values())



