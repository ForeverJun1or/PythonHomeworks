import re
from datetime import datetime

import CurrencyExchange

if __name__ == "__main__":
    while (True):
        str_date = input("На яку дату Ви бажаєте отримати курс валют? Дата вводиться у форматі дд.мм.рррр. Наприклад: 01.01.2022\n")
        # Перевірка за допомогою регулярного виразу, чи дійсно користувач правильно надіслав дату
        re_pattern = '(0[1-9]|[12][0-9]|3[01]).(0?[1-9]|1[012]).(20[0-2]\d)$'
        if re.match(re_pattern, str_date):
            user_date = datetime.strptime(str_date, '%d.%m.%Y').date()
            if user_date > datetime.now().date():
                continue
            break

    # Якщо дату введено вірно, то запускається метод get_cur_exchange(user_date) з класу ExchangeNBU і якщо він
    # коректно відпрацював, то повертає True, та користувач сповіщається про успішну операцію. Якщо ж виникла помилка
    # користувач також побачить повідомлення про це, а інформація про помилку буде знаходитись у файлі log.txt
    if CurrencyExchange.ExchangeNBU.get_cur_exchange(user_date):

        print(f'Звіт по курсу валют сформовано у файл \'{user_date.strftime("%d_%m_%Y")}_NBU.txt\'')
    else:
        print('Виникла помилка при спробі сформувати звіт. Подробиці у файлі \'log.txt\'')
