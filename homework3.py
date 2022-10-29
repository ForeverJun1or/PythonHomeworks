# Напишіть код, який зформує строку, яка містить певну інформацію про символ за його номером у слові. Наприклад "The [номер символу] symbol in '[тут слово]' is
# '[символ з відповідним порядковим номером в слові]'". Слово та номер символу отримайте за допомогою input() або скористайтеся константою. Наприклад
# (слово - "Python" а номер символу 3) - "The 3 symbol in 'Python' is 't' ".
print("Завдання 1")
userstring = input("Введіть будь-яке слово. Наприклад: \"Restricted\".\n")
while not userstring or len(userstring.split()) > 1:
    userstring = input("Невірний формат, введіть слово ще раз. Наприклад: \"Restricted\".\n")

usernumber = input(
    f"Введіть будь-який порядковий номер символу у слові \"{userstring}\" для його відображення. Наприклад: 1.\n")
while True:
    if not usernumber.isnumeric():
        usernumber = input("Невірний формат, введіть номер ще раз.  Наприклад: 1.\n")
        continue
    usernumber = int(usernumber)
    userstringlength = len(userstring)
    if usernumber > userstringlength:
        usernumber = input(
            f"У слові {userstring} всього {userstringlength} літер. Введіть число від 1 до {userstringlength}\n")
        continue
    else:
        print(
            f"Під номером {usernumber} у слові \"{userstring}\" знаходиться літера \"{userstring[usernumber - 1]}\"\n\n")
    break

# Вести з консолі строку зі слів за допомогою input() (або скористайтеся константою). Напишіть код, який визначить кількість слів, в цих даних.
print("Завдання 2")
userstring = input("Введіть будь-яке речення з двох чи більше слів. Наприклад \"Час вставати на роботу\".\n")
while not userstring or len(userstring.split()) < 2:
    userstring = input("Невірний формат, введіть речення ще раз. Наприклад \"Час вставати на роботу \".\n")
print(f"Кількість слів у реченні \"{userstring}\" дорівнює {len(userstring.split())}\n\n")

# Існує ліст з різними даними, наприклад lst1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum'].
# Напишіть код, який сформує новий list (наприклад lst2), який би містив всі числові змінні (int, float), які є в lst1.
# Майте на увазі, що данні в lst1 не є статичними можуть змінюватись від запуску до запуску.
print("Завдання 3")
lst1 = ["1", "2", 3, True, "False", 5, "6", 7, 8, "Python", 9, 0, "Lorem Ipsum", 5.5, "3.2"]
lst2 = []
for el in lst1:
    if (type(el) == int or type(el) == float):
        lst2.append(el)
print(lst2)
