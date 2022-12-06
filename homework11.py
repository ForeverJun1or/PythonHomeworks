import abc


class Vehicle(abc.ABC):
    make_year: int = 0
    speed: int | float = 0
    cost: int = 0

    @abc.abstractmethod
    def get_info(self):
        pass


class Auto(Vehicle):
    brand: str = ''
    model: str = ''

    def __init__(self, make_year, speed, cost, brand, model):
        self.make_year = make_year
        self.speed = speed
        self.cost = cost
        self.brand = brand
        self.model = model

    def get_info(self):
        print(
            f'Це автомобіль {self.brand} {self.model}, який було вироблено у {self.make_year} році. Він розганяється до {self.speed} кілометрів на годину та коштує {self.cost}$.')


class Plane(Vehicle):
    brand: str = ''
    model: str = ''
    height: int = 0
    number_of_passengers: int = 0

    def get_info(self):
        print(
            f'Це літак {self.brand} {self.model}, який було вироблено у {self.make_year} році. Він летить зі швидкістю до {self.speed} кілометрів на годину, підіймається на висоту до {self.height} м., вміщує до {self.number_of_passengers} пасажирів та коштує {self.cost}$.')


class Ship(Vehicle):
    name: str = ''
    destination_port: str = ''
    number_of_passengers: int = 0
    __chief_computer_password: str = '12345'

    def __init__(self, make_year, speed, cost, name, destination_port, number_of_passengers):
        self.make_year = make_year
        self.speed = speed
        self.cost = cost
        self.name = name
        self.destination_port = destination_port
        self.number_of_passengers = number_of_passengers

    def get_info(self):
        print(
            f'Це корабель {self.name}, який було вироблено у {self.make_year} році. Він пливе зі швидкістю до {self.speed} вузлів, прямує до порту {self.destination_port}, вміщує до {self.number_of_passengers} пасажирів та коштує {self.cost}$.')


auto = Auto(2020, 180, 36000, 'Toyota', 'Prius')
auto.get_info()

plane = Plane()
plane.brand = 'Airbus'
plane.model = 'A380'
plane.make_year = 2007
plane.speed = 900
plane.cost = 489000000
plane.number_of_passengers = 853
plane.height = 13115
plane.get_info()

ship = Ship(2008, 22.6, 1400000000, 'Oasis of the Seas', 'Сафага, Хургада', 5400)
ship.get_info()
