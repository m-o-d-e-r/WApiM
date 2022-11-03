from fastapi import FastAPI

from .apps.random.app import random_app
from .apps.weather.app import weather_app


app = FastAPI()

app.include_router(random_app)
app.include_router(weather_app)
