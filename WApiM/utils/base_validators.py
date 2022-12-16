
def is_valid_length_value(value: int):
    """Перевідка правильності довжини масиву"""

    if isinstance(value, int):
        return value > 0
    
    return False
