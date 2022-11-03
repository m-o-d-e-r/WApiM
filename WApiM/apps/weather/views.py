from pprint import pprint

from pyowm import OWM
from pyowm.commons.exceptions import NotFoundError

from .models import (
    RequestWeather,
    ResponseError,
    ResponseCityData,
    ResponseWeather
)


owm_object = OWM("67cec42b4ac92cb28ee8999242b3a14b")
owm_manager = owm_object.weather_manager()


async def __get_weather_data(r: RequestWeather, current_city_name: str = "") -> ResponseCityData | str:
    city_name = r.city if not current_city_name else current_city_name

    try:
        weather = owm_manager.weather_at_place(city_name).weather
    except NotFoundError:
        return f"Invalid city name > {city_name}"
    except:
        return "Server error"

    return ResponseCityData(
        city=city_name,
        temperature=weather.temperature("celsius") if r.temperature else False,
        humidity=weather.humidity if r.humidity else False,
        wind_data=weather.wind() if r.wind_data else False
    )



async def get_weather_at(r: RequestWeather):
    weather_data: ResponseCityData | list[ResponseCityData] = []

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

    return ResponseWeather(weather=weather_data)
