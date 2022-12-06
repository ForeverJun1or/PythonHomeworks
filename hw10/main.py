from library import exponent_multiplication


def try_convert_to_number(value: str):
    if value.isnumeric() or value.replace("-", "").isnumeric():
        return int(value)
    elif value.replace(".", "").isnumeric() or value.replace(".", "").replace("-", "").isnumeric():
        return float(value)


def is_number(*args):
    for arg in args:
        if not isinstance(arg, (int, float)):
            return False
    return True


def start():
    print("Вітаю! Ця програма вміє приймати 2 числових значення, множити їх та піднесити результат множення до степеня.")
    first_number = try_convert_to_number(input("Введіть числове значення №1:\n"))
    second_number = try_convert_to_number(input("Введіть числове значення №2\n"))
    exponent = try_convert_to_number(input("Введіть ступінь (числове значення):\n"))
    result = None
    if is_number(first_number, second_number, exponent):
        result = exponent_multiplication(first_number, second_number, exp=exponent)
    print(f'Результат дорівнює {result}.') if result is not None else print(
        "Сталася помилка. Можливо, одне з введених значень не було числовим.")


if __name__ == "__main__":
    start()
