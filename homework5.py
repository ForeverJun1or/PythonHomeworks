import requests
def get_json(url):
    try:
        response = requests.get(url)
        if not response.ok:
            raise Exception(response.json())
        return response.json()
    except Exception as inst:
        print(f'An error occured: {inst}')
        return {}

# завдання 1
# урл http://api.open-notify.org/astros.json#
# вивести список всіх астронавтів, що перебувають в даний момент на орбіті (дані не фейкові, оновлюються в режимі реального часу)
print('Завдання №1')
if content := get_json('http://api.open-notify.org/astros.json'):
    print('На даний момент на орбіті перебувають наступні астронавти:')
    for astronaut in content['people']:
        print(astronaut['name'])


# Завдання 2
# апі погоди (всі токени я для вас вже прописав)
# https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid=47503e85fabbabc93cff28c52398ae97&units=metric
# де city_name - назва міста на аглійській мові (наприклад, odesa, kyiv, lviv)
# погода змінюється, як і місто. яке ви введете
# роздрукувати тепрературу та швидкість вітру. з вказівкою міста, яке було вибране
print('\n\nЗавдання №2')
if content := get_json('https://api.openweathermap.org/data/2.5/weather?q=dnipro&appid=47503e85fabbabc93cff28c52398ae97&units=metric'):
    city = content['name']
    temp = content['main']['temp']
    wind_gust = content['wind']['gust']
    wind_speed = content['wind']['speed']
    print(f'У місті {city} на цю хвилину температура складає {int(temp)}°C, швидкість вітру {wind_speed} м/с, пориви до {wind_gust} м/с')