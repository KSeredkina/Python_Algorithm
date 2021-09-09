"""4. Определить, какое число в массиве встречается чаще всего."""
import random

# array_numbers = [2, 3, 4, 2, 45, 3, 45, 5, 2]
array_numbers = []
for number in range(10):
    array_numbers.append(random.randint(0, 99))
print(f'Заданный массив: {array_numbers}')

number = array_numbers[0]
max_count = 1
for i in range(len(array_numbers) - 1):
    count = 1
    for j in range(i + 1, len(array_numbers)):
        if array_numbers[i] == array_numbers[j]:
            count += 1
        if count > max_count:
            max_count = count
            number = array_numbers[i]
if max_count > 1:
    print(max_count, 'раз(а) встречается число', number)
else:
    print('Все элементы уникальны')
