
def is_valid_range(a: int | float, b: int | float) -> tuple[bool, str]:
    """Перевірка валідності діапазону чисел"""

    if (a == b):
        return (False, "from_ parameter is equal to to_")
    elif (a > b):
        return (False, "from_ parameter is greater that to_")

    return (True, "")


def is_valid_operation(operation: str):
    """Перевірка валідності оператора для обчислення"""

    __available_op = ("*", "+")
    return operation in __available_op
