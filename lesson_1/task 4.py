"""4. Написать программу, которая генерирует в указанных пользователем границах:
случайное целое число;
случайное вещественное число;
случайный символ.
Для каждого из трех случаев пользователь задает свои границы диапазона.
Например, если надо получить случайный символ от 'a' до 'f', то вводятся эти символы. Программа должна вывести на
экран любой символ алфавита от 'a' до 'f' включительно. """
from random import random

type_range, begin_range, end_range = [i for i in input('Введите тип генерируемого значения (int, float, symbol) и '
                                                       'границы диапазона через пробел: ').split()]
if type_range == 'int':
    number_integer = int(random() * (int(end_range) - int(begin_range) + 1)) + int(begin_range)
    print(f'Случайное целое число в заданном диапазоне: {number_integer}')
elif type_range == 'float':
    number_float = random() * (float(end_range) - float(begin_range)) + float(begin_range)
    print(f'Случайное вещественное число в заданном диапазоне: {round(number_float, 2)}')
elif type_range == 'symbol':
    number_symbol = int(random() * (ord(end_range) - ord(begin_range)) + ord(begin_range))
    print(f'Случайный символ в заданном диапазоне: {chr(number_symbol)}')
else:
    print(f'Неверно заданы границы диапазона или тип генерируемого значения')
