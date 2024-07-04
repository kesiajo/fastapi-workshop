# FastAPI Tutorial

## Setup
Set up your virtual environment
```bash
python -m venv env
.\env\Scripts\activate
pip install -r requirements.txt
```
If you're running Linux or MacOS you'll instead run
```bash
python -m venv env
source ./env/bin/activate
pip install -r requirements.txt
```

Using Poetry
```bash
poetry init
poetry add fastapi
```

## Running the app
`uvicorn main:app --reload`