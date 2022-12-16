from typing import Any

from pydantic import BaseModel


class RequestWeatherAt(BaseModel):
    """
        Шаблон користувацького запиту
        для отримання погоди в конкретному місці планети
    """
    city: str | list
    temperature: bool = True
    humidity: bool | None
    wind_data: bool | None


class ResponseCityDataAt(BaseModel):
    """
        Шаблон відповіді сервера на запит про
        отримання погоди в конкретному місці
    """
    city: str
    temperature: Any
    humidity: Any
    wind_data: Any


class ResponseWeatherAt(BaseModel):
    """
        Шаблон відповіді сервера на запит про
        отримання погоди в декількох місцях планети

        :weather - список де будуть зберігатися погодні дані

    """
    weather: ResponseCityDataAt | list[ResponseCityDataAt]



class RequestWeatherRandom(BaseModel):
    """
        Шаблон запиту для отримання випадкових погодних даних

        :data_set_len - кількість випадкових місць планети

    """
    data_set_len: int


class RandomWeatherItem(BaseModel):
    """
        Фільтрація по даним які хоче отримувати користувач

    """
    temperature: Any
    humidity: Any
    wind_data: Any


class ResponseWeatherRandom(BaseModel):
    """
        Шаблон відповіді сервера на запит про
        отримання погоди в декількох випадкових місцях планети

        :weather - список де будуть зберігатися погодні дані

    """
    weather: list[RandomWeatherItem]
