from Figures import Point, Triangle


def create_triangle():
    first_point = Point(0, 0)
    second_point = Point(0, 5)
    third_point = Point(5, 0)
    triangle1 = Triangle(first_point, second_point, third_point)
    print(
        f'Створено трикутник №1 зі сторонами:\n1:{first_point.x},{first_point.y}\n2:{second_point.x},{second_point.y}\n3:{third_point.x},{third_point.y}')
    triangle1_area = triangle1.area()
    print(str(triangle1))
    first_point2 = Point(0, 0)
    second_point2 = Point(0, 6)
    third_point2 = Point(5, 0)
    triangle2 = Triangle(first_point2, second_point2, third_point2)
    print(
        f'Створено трикутник №2 зі сторонами:\n1:{first_point2.x},{first_point2.y}\n2:{second_point2.x},{second_point2.y}\n3:{third_point2.x},{third_point2.y}')
    triangle2_area = triangle2.area()
    print(f'Площа трикутника №1 дорівнює {triangle1_area}')
    print(f'Площа трикутника №2 дорівнює {triangle2_area}')
    print(f'Трикутник №1 дорівнює Трикутнику №2: {triangle1 == triangle2}')
    print(f'Трикутник №1 не дорівнює Трикутнику №2: {triangle1 != triangle2}')
    print(f'Трикутник №1 більший, аніж Трикутник №2: {triangle1 > triangle2}')
    print(f'Трикутник №1 меньший, аніж Трикутник №2: {triangle1 < triangle2}')
    print(f'Трикутник №1 більший або дорівнює Трикутнику №2: {triangle1 >= triangle2}')
    print(f'Трикутник №1 меньший або дорівнює Трикутнику №2: {triangle1 <= triangle2}')


if __name__ == "__main__":
    create_triangle()
