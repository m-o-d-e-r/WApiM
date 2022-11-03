from typing import Any

from pydantic import BaseModel


class RequestWeather(BaseModel):
    city: str | list
    temperature: bool = True
    humidity: bool | None
    wind_data: bool | None


class ResponseError(BaseModel):
    info: str
    data: dict


class ResponseCityData(BaseModel):
    city: str
    temperature: Any
    humidity: Any
    wind_data: Any


class ResponseWeather(BaseModel):
    weather: ResponseCityData | list[ResponseCityData]
