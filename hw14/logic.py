from random import choice


class GameFigure:
    """Class GameFigure what contains types of figures and the functions of compare"""
    types_of_figures = [
        "rock",
        "scissors",
        "paper",
        "lizard",
        "spock",
    ]
    figure = None

    def __init__(self, figure: str):
        self.figure = figure

    def __eq__(self, other):
        return self.figure == other.figure if isinstance(other, GameFigure) else False

    def __gt__(self, other):
        if isinstance(other, GameFigure):
            match self.figure:
                case 'rock':
                    return True if other.figure == 'scissors' or other.figure == 'lizard' else False
                case 'paper':
                    return True if other.figure == 'rock' or other.figure == 'spock' else False
                case 'scissors':
                    return True if other.figure == 'paper' or other.figure == 'lizard' else False
                case 'lizard':
                    return True if other.figure == 'spock' or other.figure == 'paper' else False
                case 'spock':
                    return True if other.figure == 'scissors' or other.figure == 'rock' else False


class Player:
    """Class Player what contains variable player_type (human or computer) which determined when the class is
    initialized and variable player_figure what save player selected figure inside"""
    _player_type = None
    player_figure = None

    def __init__(self, player_type: str):
        if not isinstance(player_type, str):
            raise TypeError
        if player_type != 'human' or player_type != 'computer':
            raise ValueError
        self._player_type = player_type

    def choose_figure(self):
        """func that check the type of player and than if it a human, suggest him to choose the figure.
        If it the computer, then the figure choise by the func choise from the Random module"""
        if self._player_type == 'human':
            while True:
                player_input = input(
                    "Оберіть один з варіантів:\n1 - rock\n2 - scissors\n3 - paper\n4 - lizard\n5 - spock\n\n")
                try:
                    self.player_figure = GameFigure(GameFigure.types_of_figures[int(player_input) - 1])
                except Exception:
                    continue
                break
            return
        self.player_figure = GameFigure(choice(GameFigure.types_of_figures))


class Game:
    first_player = Player('human')
    second_player = None
    result = None

    def __init__(self):
        """First func where we create Game class instance in the main.py. It calls next func named start_game"""
        self.start_game()

    def start_game(self):
        """Main func in the program what calls other functions in order:
        choose_game_mode()
        choose_the_figures()
        get_result()
        """
        print('Гра почалася!')
        self.choose_game_mode()
        self.choose_the_figures()
        self.result = self.get_result()

    def choose_game_mode(self):
        """func that prompts the player to choose a game mode
        and based on the choice determines the type of the second player in the variable second_player"""
        while True:
            playing_with = input('Ви бажаєте зіграти з комп\'ютером або удвох?\n'
                                 '1: З комп\'ютером\n'
                                 '2: удвох\n')
            match playing_with:
                case '1':
                    self.second_player = Player('computer')
                case '2':
                    self.second_player = Player('human')
                case _:
                    continue
            break

    def choose_the_figures(self):
        """suggest players to choose the figures"""
        self.first_player.choose_figure()
        print(f'Гравець №1 обрав: {self.first_player.player_figure.figure}')
        self.second_player.choose_figure()
        print(f'Гравець №2 обрав: {self.second_player.player_figure.figure}')

    def get_result(self):
        """call the func what compares figures with each other and determines the result"""
        if self.first_player.player_figure == self.second_player.player_figure:
            return 'Нічия'
        elif self.first_player.player_figure > self.second_player.player_figure:
            return f'{self.first_player.player_figure.figure} б\'є {self.second_player.player_figure.figure}, тому гравець №1 переміг'
        else:
            return f'{self.second_player.player_figure.figure} б\'є {self.first_player.player_figure.figure}, тому гравець №2 переміг'

    def result_announcement(self):
        """announcement result"""
        print(f'{self.result}\n\n')
