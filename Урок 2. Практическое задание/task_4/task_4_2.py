"""
4.	Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
Количество элементов (n) вводится с клавиатуры.

Пример:
Введите количество элементов: 3
Количество элементов - 3, их сумма - 0.75

ЗДЕСЬ ДОЛЖНА БЫТЬ РЕАЛИЗАЦИЯ ЧЕРЕЗ РЕКУРСИЮ
"""


def row_sum(k, s, m):
    if k > 1:
        m = - m / 2
        s = s + m
        k -= 1
        return row_sum(k, s, m)
    else:
        return s


while True:
    try:
        K = int(input('Введите колличество элементов: '))
        break
    except ValueError:
        print('Некорректный ввод. Введите целое число')
S = 1
M = 1
print(f'сумма элементов: {row_sum(K, S, M)}')
