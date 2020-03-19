"""
3.	Сформировать из введенного числа обратное по порядку входящих в него
цифр и вывести на экран. Например, если введено число 3486,
 то надо вывести число 6843.

Подсказка:
На каждом шаге вам нужно 'доставать' из числа очередную цифру
Пока все числа не извлечены рекурсивные вызовы продолжаем
Условие завершения рекурсии - все числа извлечены

Пример:
Введите число, которое требуется перевернуть: 123
Перевернутое число: 321

ЗДЕСЬ ДОЛЖНА БЫТЬ РЕАЛИЗАЦИЯ ЧЕРЕЗ РЕКУРСИЮ
"""


def revertion(n, n2):
    if n // 10 != 0:
        k = n % 10
        n = n // 10
        n2 = n2 * 10 + k
        return revertion(n, n2)
    else:
        n2 = n2 * 10 + n
        return n2


while True:
    try:
        N1 = int(input('Введите число: '))
        break
    except ValueError:
        print('Некорректный ввод. Введите целое число')

N2 = 0

print(f'перевернутое число: {revertion(N1, N2)}')
