"""5. Пользователь вводит две буквы. Определить, на каких местах алфавита они стоят и сколько между ними находится
букв. """

letter_1, letter_2 = map(lambda x: x.upper(), input('Введите две буквы, через пробел (A - Z): ').split())

alphabet_list = [chr(i) for i in range(ord('A'), ord('Z') + 1)]
index_letter_1 = alphabet_list.index(letter_1) + 1
index_letter_2 = alphabet_list.index(letter_2) + 1

if index_letter_1 < index_letter_2:
    step = 1
else:
    step = -1

print(f'Первая буква {letter_1} находится на позиции: {index_letter_1}')
print(f'Вторая буква {letter_2} находится на позиции: {index_letter_2}')
print(f'Между ними букв: {abs(index_letter_1 - index_letter_2) - 1}')
