# Завдання 1
# Напишіть функцію, що приймає один аргумент будь-якого типу та повертає цей аргумент, перетворений на float.
# Якщо перетворити не вдається функція має повернути 0.
print('Завдання №1')


def val_to_float(val):
    try:
        return float(val)
    except Exception as ex:
        print(ex.args)
        return 0


result = val_to_float(input("Введіть будь яке число: "))
print(f'Значення {result}. Тип:{type(result)}')

# # Завдання 2
# # Напишіть функцію, що приймає два аргументи. Функція повинна
# # якщо аргументи відносяться до числових типів (int, float) - повернути перемножене значення цих аргументів,
# # якщо обидва аргументи це строки (str) - обʼєднати в одну строку та повернути
# # у будь-якому іншому випадку повернути кортеж з цих аргументів
print('\n\nЗавдання №2')


def try_parse(val1):
    # res = val1
    try:
        val1 = int(val1)
    except:
        val1 = float(val1)
    finally:
        return val1


def multiply_values(val1, val2):
    val1 = try_parse(val1)
    val2 = try_parse(val2)
    if (type(val1) == int or type(val1) == float) and (type(val2) == int or type(val2) == float):
        return val1 * val2
    elif type(val1) == str and type(val2) == str:
        return val1 + val2
    else:
        return val1, val2


val1 = input('Введіть аргумент №1: ')
val2 = input('Введіть аргумент №2: ')
result = multiply_values(val1, val2)
print(f'Значення {result}. Тип:{type(result)}')

# Завдання 3
# Перепишіть за допомогою функцій вашу программу "Касир в кінотеатрі", яка буде виконувати наступне:
# Попросіть користувача ввести свсвій вік.
# - якщо користувачу менше 7 - вивести "Тобі ж <> <>! Де твої батьки?"
# - якщо користувачу менше 16 - вивести "Тобі лише <> <>, а це е фільм для дорослих!"
# - якщо користувачу більше 65 - вивести "Вам <> <>? Покажіть пенсійне посвідчення!"
# - якщо вік користувача містить 7 - вивести "Вам <> <>, вам пощастить"
# - у будь-якому іншому випадку - вивести "Незважаючи на те, що вам <> <>, білетів всеодно нема!"
# Замість <> <> в кожну відповідь підставте значення віку (цифру) та правильну форму слова рік.
# Для будь-якої відповіді форма слова "рік" має відповідати значенню віку користувача (1 - рік, 22 - роки, 35 - років і тд...).
print('\n\nЗавдання №3')


def correct_write(age):
    age = str(age)
    d = age[-1]
    var1 = '1'
    var2 = '234'
    var3 = '567890'
    if age in range(10,20):
        return 'років'
    elif age[-1] in var1:
        return 'рік'
    elif age[-1] in var2:
        return 'роки'
    elif age[-1] in var3:
        return 'років'


def age_process(age):
    res = ''
    age = try_parse(age)
    correct_age = correct_write(age)
    if (type(age) == int):
        if (age < 1):
            res = 'Вам не може бути меньше 1 року'
        elif (age > 122):
            res = f'Рекорд довготривалості життя був зафіксований у Франції і склав 122 роки. Я думаю, що вам не може бути {age} {correct_age}...'
        elif ('7' in str(age)):
            res = f'Вам {age} {correct_age}, вам пощастить!'
        elif (age <7):
            res = f'Тобі ж {age} {correct_age}! Де твої батьки?'
        elif (age < 16):
            res = f'Тобі лише {age} {correct_age}, а це е фільм для дорослих!'
        elif (age > 65):
            res = f'Вам {age} {correct_age}? Покажіть пенсійне посвідчення!'
        else:
            res = f'Незважаючи на те, що вам {age} {correct_age}, білетів всеодно нема!'
    return res


result = age_process(input('Введіть свій вік: '))
print(result)
