from pydantic import BaseModel


class UserResponseModel(BaseModel):
    token: str
    count: int


class BaseWeatherResponseModel(BaseModel):
    user: UserResponseModel


class RandomWeatherResponseModel(BaseWeatherResponseModel):
    ...


class WeatherResponseModel(BaseWeatherResponseModel):
    ...
