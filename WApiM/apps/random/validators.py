
def is_valid_range(a: int | float, b: int | float) -> tuple[bool, str]:
    if (a == b):
        return (False, "from_ parameter is equal to to_")
    elif (a > b):
        return (False, "from_ parameter is greater that to_")

    return (True, "")


def is_valid_list_kwargs(range_len: int | None, sorted_: bool | None) -> tuple[bool, str]:
    if (not isinstance(range_len, int) and isinstance(sorted_, bool)):
        return (False, "Range len is not defined")

    if (isinstance(range_len, int) and range_len < 1):
        return (False, "Range len must be greater that 0")

    return (True, "")




def is_valid_operation(operation: str):
    __available_op = ("*", "|")

    return operation in __available_op
