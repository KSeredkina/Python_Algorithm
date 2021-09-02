"""6. Пользователь вводит номер буквы в алфавите. Определить, какая это буква."""

letter_number = int(input('Введите номер буквы в алфавите: '))

alphabet_list = [chr(i) for i in range(ord('A'), ord('Z') + 1)]
# print(alphabet_list)
if letter_number <= len(alphabet_list):
    print(f'Буква под номером {letter_number}: {alphabet_list[letter_number - 1]}')
else:
    print(f'Введено число превышающее количество букв в алфавите ({len(alphabet_list)})')
