from random import uniform

from pyowm import OWM
from pyowm.commons.exceptions import NotFoundError

from ...utils.base_models import ResponseError
from ...utils.base_validators import is_valid_length_value
from .models import (
    RequestWeatherAt,
    ResponseCityDataAt,
    ResponseWeatherAt
)
from .models import (
    RequestWeatherRandom,
    RandomWeatherItem,
    ResponseWeatherRandom
)
from .apikey import API_KEY


owm_object = OWM(API_KEY)
owm_manager = owm_object.weather_manager()


async def __get_weather_data(r: RequestWeatherAt, current_city_name: str = "") -> ResponseCityDataAt | str:
    city_name = r.city if not current_city_name else current_city_name

    try:
        weather = owm_manager.weather_at_place(city_name).weather
    except NotFoundError:
        return f"Invalid city name > {city_name}"
    except:
        return "Server error"

    return ResponseCityDataAt(
        city=city_name,
        temperature=weather.temperature("celsius") if r.temperature else False,
        humidity=weather.humidity if r.humidity else False,
        wind_data=weather.wind() if r.wind_data else False
    )



async def get_weather_at(r: RequestWeatherAt):
    weather_data: ResponseCityDataAt | list[ResponseCityDataAt] = []

    if isinstance(r.city, str):
        weather_data = await __get_weather_data(r)

        if isinstance(weather_data, str):
            return ResponseError(
                info=weather_data,
                data=r.dict()
            )
    else:
        temp_weather = None
        for city_name in r.city:
            temp_weather = await __get_weather_data(r, city_name)
            if isinstance(temp_weather, str):
                return ResponseError(
                    info=temp_weather,
                    data=r.dict()
                )
            weather_data.append(temp_weather)

    return ResponseWeatherAt(weather=weather_data)


async def get_weather_random(r: RequestWeatherRandom):
    weather_data: list[RandomWeatherItem] = []

    if not is_valid_length_value(r.data_set_len):
        return ResponseError(
            info="Length value is invalid",
            data=r.dict()
        )

    weather_in_cords = None
    for i in range(r.data_set_len):
        weather_in_cords = owm_manager.weather_at_coords(
            uniform(-90, 90),
            uniform(-90, 90)
        ).weather

        weather_data.append(
            RandomWeatherItem(
                temperature=weather_in_cords.temperature("celsius"),
                humidity=weather_in_cords.humidity,
                wind_data=weather_in_cords.wind()
            )
        )

    return ResponseWeatherRandom(weather=weather_data)
