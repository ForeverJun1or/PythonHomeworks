# Напишіть гру "rock scissors paper lizard spock".
# Використайте розділення всієї програми на функції (Single-Responsibility principle). Я
# к скелет-заготовку можна використати приклад з заняття.
# До кожної функції напишіть докстрінг або анотацію
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
    return result


def show_message_to_user(message):
    """Notifies player about smth (get from arg)"""
    print(f"{message}")


def get_players_answer(question):
    """Asks the player if he wants to continue the game and wait for his answer, then analyze and returns"""
    while True:
        player_answer = input(question)
        if player_answer in "12":
            return player_answer


def start_game():
    """Program main function. Start all over functions, save its returns in variables if needed (inside itself)."""
    show_message_to_user("Вітаємо Вас у грі 'Камень, Ножиці, Бумага'!")
    while True:
        player_choise = get_player_choise()
        show_message_to_user(f"Ви обрали варіант: {player_choise}")
        computer_choise = get_computer_choise()
        show_message_to_user(f"Комп'ютер обрав варіант: {computer_choise}")
        result = play_game(player_choise, computer_choise)
        show_message_to_user(result)
        players_answer = get_players_answer(f"\nБажаєте зіграти ще?\n1 - Так\n2 - Ні\n")
        if players_answer == '2':
            break


start_game()
