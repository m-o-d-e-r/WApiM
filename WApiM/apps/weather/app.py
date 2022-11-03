from fastapi import APIRouter

from .views import get_weather_at


weather_app = APIRouter(prefix="/weather")

weather_app.add_api_route("/at", get_weather_at, methods=["POST"])
