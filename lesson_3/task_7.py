"""7. В одномерном массиве целых чисел определить два наименьших элемента. Они могут быть как равны между собой (оба
являться минимальными), так и различаться. """
import random

array_numbers = []
for number in range(10):
    array_numbers.append(random.randint(0, 99))
print(f'Заданный массив: {array_numbers}')

min_index_1 = 0
min_index_2 = 1
for i in range(2, len(array_numbers)):
    if array_numbers[min_index_1] > array_numbers[i]:
        min_index_2 = min_index_1
        min_index_1 = i
    elif array_numbers[min_index_2] > array_numbers[i]:
        min_index_2 = i
print(f'Два наименьших элемента: {array_numbers[min_index_1]} и {array_numbers[min_index_2]}')
