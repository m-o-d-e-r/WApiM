from pydantic import BaseModel


class ResponseError(BaseModel):
    info: str
    data: dict
