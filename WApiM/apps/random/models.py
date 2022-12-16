from pydantic import BaseModel


class RequestRandom(BaseModel):
    """Шаблон користувацького запиту для отримання випадкового числа типу int"""
    from_: int | float
    to_: int | float
    range_len: int | None
    sorted_: bool | None


class ResponseRandom(BaseModel):
    """Відповідь від сервера у вигляді числа або списку чисел"""
    number: int | float | list[int | float]


class RequestRandomWeatherNumber(BaseModel):
    """Шаблон запиту для отримання випадкового числа згенерованого на основі погоди"""
    count_weather_items: int
    temperature: bool
    humidity: bool
    wind_data: bool
    operation: str
