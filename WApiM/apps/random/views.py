import random

from .models import RequestRandom, ResponseRandom, ResponseError
from .validators import is_valid_range, is_valid_list_kwargs


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

    return ResponseRandom(number=random.uniform(r.from_, r.to_))
