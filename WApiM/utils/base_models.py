from pydantic import BaseModel


class ResponseError(BaseModel):
    """Відповідь-помилка від сервера"""

    info: str
    data: dict
