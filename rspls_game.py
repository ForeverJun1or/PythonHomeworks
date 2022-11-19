# Напишіть гру "rock scissors paper lizard spock".
# Використайте розділення всієї програми на функції (Single-Responsibility principle). Я
# к скелет-заготовку можна використати приклад з заняття.
# До кожної функції напишіть докстрінг або анотацію
from random import choice
from datetime import datetime
from os.path import exists

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


def get_player_choise():
    """Check players input, parse to int and returns one it from options

    :rtype:str
    :return:option
    """
    while True:
        player_input = input("Оберіть один з варіантів:\n1 - Камінь\n2 - Ножиці\n3 - Бумага\n4 - Ящерка\n5 - Спок\n\n")
        if player_input in "12345":
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
    return result+"\n"


def show_message_to_user(message):
    """Notifies player about smth (get from arg)"""
    print(f"{message}")


def get_players_answer(question):
    """Asks the player if he wants to continue the game and wait for his answer, then analyze and returns"""
    while True:
        player_answer = input(question)
        if player_answer =="1" or player_answer=="2":
            return player_answer


def save_result(player_choise, computer_choise, result):
    path = "stat.txt"
    stat_exists = exists(path)
    number_of_game = -1
    with open(path,"a+") as stat_file:
        if stat_exists:
            info = stat_file.read()
            f = 1
        else:
            number_of_game = 1
        stat_file.write(f"{number_of_game}. Гра відбулася {datetime.now().strftime('%d.%m.%Y %H:%M:%S')}. Користувач вибрав {player_choise}. Комп'ютер вибрав {computer_choise}. {result}\n\n")


def start_game():
    """Program main function. Start all over functions, save its returns in variables if needed (inside itself)."""
    player_choise = get_player_choise()    
    show_message_to_user(f"Ви обрали варіант: {player_choise}")
    computer_choise = get_computer_choise()
    show_message_to_user(f"Комп'ютер обрав варіант: {computer_choise}")
    result = play_game(player_choise, computer_choise)
    save_result(player_choise,computer_choise,result)
    show_message_to_user(result)