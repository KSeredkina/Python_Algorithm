"""3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы."""
import random

array_numbers = []
for number in range(10):
    array_numbers.append(random.randint(0, 99))
print(f'Исходный вид массива: {array_numbers}')

max_item = array_numbers[0]
min_item = array_numbers[0]

for item in array_numbers:
    if item > max_item:
        max_item = item
    elif item < min_item:
        min_item = item
min_index = array_numbers.index(min_item)
max_index = array_numbers.index(max_item)
array_numbers[min_index], array_numbers[max_index] = array_numbers[max_index], array_numbers[min_index]

print(f'Массив после изменения элементов ({min_index}, {max_index}): {array_numbers}')
