# Завдання 1
# Дана довільна строка. Напишіть код, який знайде в ній і віведе на екран кількість слів, які містять дві голосні літери підряд.
print('Завдання 1')
some_string = input('Введіть будь-яке речення:')
total_counter = 0;


# Варіант 1-----------------------------------------------------------------------------------------------------------------------
def Is_vowel_char(char):
    check_set = {"A", "a", "E", "e", "I", "i", "U", "u", "O", "o", "Y", "y",
                 "У", "у", "Е", "е", "Ё", "ё", "А", "а", "Ы", "ы", "О", "о", "Я", "я", "И", "и", "І", "і", "Ї", "ї",
                 "Є", "є", "Э", "э", "Ю", "ю"}
    if char in check_set:
        return True
    return False


str_array = some_string.split()
for str in str_array:
    current_symbol = 0
    for char in str:
        if current_symbol < len(str) - 1:
            if Is_vowel_char(str[current_symbol]) and Is_vowel_char(str[current_symbol + 1]):
                total_counter += 1
                break
        current_symbol += 1
print(f'алгоритм -----> У приведеному реченні дві гласні букви до ряду зустрічаються {total_counter} рази(-ів)')

# Варіант 2------------------------------------------------------------------------------------------------------------------------------------------------
import re

pattern = re.compile(r'\w*([AaEeIiUuOoYyУуЕеЁёАаЫыОоЯяИиІіЇїЄєЭэЮю]{2})\w*')
total_counter = (len(pattern.findall(some_string)))
print(f'RegEX --------> У приведеному реченні дві гласні букви до ряду зустрічаються {total_counter} рази(-ів)\n\n')

# Завдання 2
# Є два довільних числа які відповідають за мінімальну і максимальну ціну. Є Dict з назвами магазинів і цінами:
# { "cito": 47.999, "BB_studio" 42.999, "momo": 49.999, "main-service": 37.245, "buy.now": 38.324, "x-store": 37.166, "the_partner": 38.988, "store": 37.720,
# "rozetka": 38.003}. Напишіть код, який знайде і виведе на екран назви магазинів, ціни яких попадають в діапазон між мінімальною і максимальною ціною.
# Наприклад: lower_limit = 35.9
# upper_limit = 37.339
# > match: "x-store", "main-service"
print('Завдання 2')
# Варіант 1-------------------------------------------------------------------------------------------------------------------------------------------------
lower_limit = 35.9
upper_limit = 37.339
price_list = {"cito": 47.999, "BB_studio": 42.999, "momo": 49.999, "main-service": 37.245, "buy.now": 38.324,
              "x-store": 37.166, "the_partner": 38.988, "store": 37.720, "rozetka": 38.003}
total_list = []
for key, value in price_list.items():
    if value > lower_limit and value < upper_limit:
        total_list.append(key)

print(f'алгоритм ----------> {total_list}')

# Варіант 2-------------------------------------------------------------------------------------------------------------------------------------------------
total_list = list(dict(filter(lambda item: True if item[1] > lower_limit and item[1] < upper_limit else False, price_list.items())).keys())
print(f'filter функція ----> {total_list}')
