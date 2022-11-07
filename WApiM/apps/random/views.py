import random
import operator

from ...utils.base_models import ResponseError
from ...utils.base_validators import is_valid_length_value
from ..weather.views import get_weather_random
from ..weather.models import RequestWeatherRandom, ResponseWeatherRandom
from .models import RequestRandom, ResponseRandom, RequestRandomWeatherNumber
from .validators import is_valid_range, is_valid_list_kwargs, is_valid_operation


async def get_i_number(r: RequestRandom):
    validator_response =  is_valid_range(r.from_, r.to_)
    if (not validator_response[0]):
        return ResponseError(info=validator_response[1], data=r.dict())

    validator_response = is_valid_list_kwargs(r.range_len, r.sorted_)
    if (not validator_response[0]):
        return ResponseError(info=validator_response[1], data=r.dict())

    response_data: int | list = 0
    if r.range_len:
        response_data = [random.randint(r.from_, r.to_) for i in range(r.range_len)]
        if r.sorted_:
            response_data.sort()
    else:
        response_data = random.randint(r.from_, r.to_)

    return ResponseRandom(number=response_data)


async def get_f_number(r: RequestRandom):
    validator_response =  is_valid_range(r.from_, r.to_)

    if (not validator_response[0]):
        return ResponseError(info=validator_response[1], data=r.dict())

    response_data: int | list = 0
    if r.range_len:
        response_data = [random.uniform(r.from_, r.to_) for i in range(r.range_len)]
        if r.sorted_:
            response_data.sort()
    else:
        response_data = random.uniform(r.from_, r.to_)

    return ResponseRandom(number=response_data)


async def get_weather_number(r: RequestRandomWeatherNumber):
    if not is_valid_length_value(r.count_weather_items):
        return ResponseError(
            info="Length value is invalid",
            data=r.dict()
        )

    if not is_valid_operation(r.operation):
        return ResponseError(
            info="Operation is invalid",
            data=r.dict()
        )

    number = 1
    current_operation = operator.mul
    if r.operation == "*":
        number = int(number)
    else:
        number = str(number)


    random_weather_data_set: ResponseWeatherRandom =  (await get_weather_random(
        RequestWeatherRandom(data_set_len=r.count_weather_items)
    )).weather

    for weather_item in random_weather_data_set:
        number = current_operation(weather_item.temperature["temp"], number)

    return ResponseRandom(number=int(number))
