# Напишіть гру "rock scissors paper lizard spock".
# Використайте розділення всієї програми на функції (Single-Responsibility principle). Я
# к скелет-заготовку можна використати приклад з заняття.
# До кожної функції напишіть докстрінг або анотацію
from datetime import datetime
from os.path import exists
from random import choice

options = [
    "Rock",
    "Scissors",
    "Paper",
    "Lizard",
    "Spock",
]

rules = {"Rock": "Scissors_Lizard",
         "Paper": "Rock_Spock",
         "Scissors": "Paper_Lizard",
         "Lizard": "Spock_Paper",
         "Spock": "Scissors_Rock",
         }

stat_file_path = "stat.txt"


def get_last_game_num():
    """this func need to check the number of the last game. For example, if you are reboot the program

    :return: int value of the last game
    if this the first game and file 'stat.txt' not exists in the directory, function retuns 0. If Error, func returns -1
    """

    if not exists(stat_file_path):
        return 0
    with open(stat_file_path, "r") as stat:
        try:
            d1 = stat.read().splitlines()
            d1.sort(reverse=True)
            last_game_number = int(d1[0].partition('.')[0])
            return last_game_number
        except:
            return -1


def get_player_choise():
    """Check players input, parse to int and returns one it from options

    :rtype:str
    :return:option
    """
    while True:
        player_input = input("Оберіть один з варіантів:\n1 - Камінь\n2 - Ножиці\n3 - Бумага\n4 - Ящерка\n5 - Спок\n\n")
        if player_input =="1" or player_input =="2"or player_input =="3"or player_input =="4"or player_input =="5":
            option = options[int(player_input) - 1]
            return option


def get_computer_choise():
    """'Emulate' AI. Choose random option from options with choose func from random module"""
    return choice(options)


def play_game(player_choise, computer_choise):
    """Chose the winner

    :rtype:str
    :return:win message
    """
    result = ""
    if player_choise == computer_choise:
        result = "Нічия!"
    elif rules[player_choise] in computer_choise:
        result = "Вітаємо, Ви перемогли!"
    else:
        result = "Нажаль, цього разу переміг комп'ютер!"
    return result + "\n"


def show_message_to_user(message):
    """Notifies player about smth (get from arg)"""
    print(f"{message}")


def get_players_answer(question):
    """Asks the player if he wants to continue the game and wait for his answer, then analyze and returns"""
    while True:
        player_answer = input(question)
        if player_answer == "1" or player_answer == "2":
            return player_answer


def save_result(player_choise, computer_choise, result):
    global last_game_number
    number_of_game = last_game_number + 1
    with open(stat_file_path, "a+") as stat_file:
        stat_file.write(
            f"{number_of_game}. Гра відбулася {datetime.now().strftime('%d.%m.%Y %H:%M:%S')}. Користувач вибрав {player_choise}. Комп'ютер вибрав {computer_choise}. {result}\n")
    last_game_number += 1


def start_game():
    """Program main function. Start all over functions, save its returns in variables if needed (inside itself)."""
    player_choise = get_player_choise()
    show_message_to_user(f"Ви обрали варіант: {player_choise}")
    computer_choise = get_computer_choise()
    show_message_to_user(f"Комп'ютер обрав варіант: {computer_choise}")
    result = play_game(player_choise, computer_choise)
    save_result(player_choise, computer_choise, result)
    show_message_to_user(result)

last_game_number = get_last_game_num()