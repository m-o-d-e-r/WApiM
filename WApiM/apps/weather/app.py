from fastapi import APIRouter

from .views import get_weather_at, get_weather_random


weather_app = APIRouter(prefix="/weather")

weather_app.add_api_route("/at", get_weather_at, methods=["POST"])
weather_app.add_api_route("/random_cords", get_weather_random, methods=["POST"])
