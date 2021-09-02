"""9. Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого)."""

number_1, number_2, number_3 = map(int, input('Введите три разных числа, через пробел: ').split())

if number_2 < number_1 < number_3 or number_3 < number_1 < number_2:
    print(f'Средним числом является: {number_1}')
elif number_1 < number_2 < number_3 or number_3 < number_2 < number_1:
    print(f'Средним числом является: {number_2}')
else:
    print(f'Средним числом является: {number_3}')
