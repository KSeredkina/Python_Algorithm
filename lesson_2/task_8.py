"""8. Посчитать, сколько раз встречается определенная цифра в введенной последовательности чисел. Количество вводимых
чисел и цифра, которую необходимо посчитать, задаются вводом с клавиатуры. """

user_range = input('Введите последовательность чисел: ')
user_digit = input('Введите цифру для поиска: ')
count = 0
for i in user_range:
    if i == user_digit:
        count += 1
print(f'Цифра {user_digit} встречается {count} раз в последовательности {user_range}')
