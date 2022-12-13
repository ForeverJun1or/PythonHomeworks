from Figures import Point, Triangle


def create_triangle():
    first_point = Point(0, 0)
    print(f'Точка №1: х:{first_point.x} у:{first_point.y}')
    second_point = Point(0, 5)
    print(f'Точка №2: х:{second_point.x} у:{second_point.y}')
    third_point = Point(5, 0)
    print(f'Точка №3: х:{third_point.x} у:{third_point.y}')

    triangle1 = Triangle(first_point, second_point, third_point)
    triangle1_area = triangle1.area()
    print(f'Площа трикутника дорівнює {triangle1_area}')
    print(str(triangle1))

    triangle2 = Triangle(Point(0,0),Point(0,5),Point(5,0))
    triangle2_area = triangle2.area()
    print(triangle1 == triangle2)
if __name__ == "__main__":
    create_triangle()
