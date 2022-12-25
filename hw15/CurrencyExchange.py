import abc
from datetime import date, datetime
import requests


class Exchange(abc.ABC):
    """Abstract class Exchange if i'll implemented not only NBU exchange"""
    @staticmethod
    @abc.abstractmethod
    def get_cur_exchange(user_date: date):
        pass

    @staticmethod
    @abc.abstractmethod
    def __get_info(user_date: date):
        pass

    @staticmethod
    @abc.abstractmethod
    def __save_info(str_result: str, user_date: date):
        pass


class ExchangeNBU(Exchange):
    """I decided to make all methods static, cause at the moment, the class functionality does not imply any variables.
    In general, the class has 3 functions, 2 of which are hidden from the user (private), and all functionality is
    implemented through a call to the get_cur_exchange function"""
    @staticmethod
    def get_cur_exchange(user_date: date):
        try:
            str_result = ExchangeNBU.__get_info(user_date)
            ExchangeNBU.__save_info(str_result, user_date)
            return True
        except Exception as e:
            with open('log.txt', 'w') as file:
                file.write(f'{datetime.now().strftime("%d.%m.%Y %H:%M:%S")} {e}\n')
            return False

    @staticmethod
    def __get_info(user_date: date):
        str_result = ''
        res = requests.request('GET',
                               f'https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?date={user_date.strftime("%Y%m%d")}&json')
        if res:
            if 'application/json' in res.headers.get('Content-Type', ''):
                response_json = res.json()
                current_position = 1
                for unit in response_json:
                    currency_name = unit.get('txt')
                    currency_short_name = unit.get('cc')
                    currency_rate = unit.get('rate')
                    str_result += f'{current_position}. {currency_name}({currency_short_name}) to UAH: {currency_rate}\n'
                    current_position += 1
        return str_result

    @staticmethod
    def __save_info(str_result: str, user_date: date):
        filename = f'{user_date.strftime("%d_%m_%Y")}_NBU.txt'
        with open(filename, 'w') as file:
            file.write(str_result)
        return True
