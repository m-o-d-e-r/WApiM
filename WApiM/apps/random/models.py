from pydantic import BaseModel


class RequestRandom(BaseModel):
    from_: int | float
    to_: int | float
    range_len: int | None
    sorted_: bool | None


class ResponseRandom(BaseModel):
    number: int | list


class RequestRandomWeatherNumber(BaseModel):
    count_weather_items: int
    temperature: bool
    humidity: bool
    wind_data: bool
    operation: str
