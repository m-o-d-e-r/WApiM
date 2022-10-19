from pydantic import BaseModel


class UserRequestModel(BaseModel):
    id: int
    name: str
    token: str
    count: int


class BaseWeatherRequestModel(BaseModel):
    user: UserRequestModel


class RandomWeatherRequestModel(BaseWeatherRequestModel):
    char_start: str | None
    char_end: str | None
    weather: int = 1


class WeatherRequestModel(BaseWeatherRequestModel):
    city: str
