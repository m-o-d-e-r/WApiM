from typing import Any

from pydantic import BaseModel


class RequestWeatherAt(BaseModel):
    city: str | list
    temperature: bool = True
    humidity: bool | None
    wind_data: bool | None


class ResponseCityDataAt(BaseModel):
    city: str
    temperature: Any
    humidity: Any
    wind_data: Any


class ResponseWeatherAt(BaseModel):
    weather: ResponseCityDataAt | list[ResponseCityDataAt]



class RequestWeatherRandom(BaseModel):
    data_set_len: int


class RandomWeatherItem(BaseModel):
    temperature: Any
    humidity: Any
    wind_data: Any


class ResponseWeatherRandom(BaseModel):
    weather: list[RandomWeatherItem]
