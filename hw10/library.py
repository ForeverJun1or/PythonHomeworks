def exponent_multiplication(first_val: int | float, second_val: int | float, /, *, exp: int | float) -> int | float:
    if exp < 1:
        raise ValueError
    result = (first_val * second_val) ** exp
    return result
