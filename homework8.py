from rspls_game import start_game
from rspls_game import get_players_answer
player_answer = get_players_answer("Вітаємо Вас у грі 'Камень, Ножиці, Бумага'!\nСкільки разів бажаєте зіграти?\n1 - я не азартний, бажаю зіграти лишень один раз.\n2 - граю до вечора!\n")
while True:
    start_game()
    if player_answer=="1":
        break
print("Дякую, що завітали на гру!")