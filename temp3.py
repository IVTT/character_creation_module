"""Оформление кода"""
from math import sqrt


def calculate_square_root(number):
    """Вычисляет квадратный корень."""
    return sqrt(number)


def calc(your_number):
    """Проверка и печать результатов."""
    if your_number <= 0:
        return
    result = calculate_square_root(your_number)
    print(
        f'Мы вычислили квадратный корень из введённого вами числа. '
        f'Это будет: {result}'
    )


print('Добро пожаловать в самую лучшую '
      'программу для вычисления квадратного корня из заданного числа.')
calc(25.5)
