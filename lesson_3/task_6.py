"""6. В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами. Сами
минимальный и максимальный элементы в сумму не включать. """
import random

array_numbers = []
for number in range(10):
    array_numbers.append(random.randint(0, 99))
print(f'Заданный массива: {array_numbers}')

min_index = 0
max_index = 0
sum_element = 0
for i in range(1, len(array_numbers)):
    if array_numbers[min_index] > array_numbers[i]:
        min_index = i
    elif array_numbers[max_index] < array_numbers[i]:
        max_index = i
if min_index > max_index:
    min_index, max_index = max_index, min_index
for i in range(min_index+1, max_index):
    sum_element += array_numbers[i]
print(f'Сумма элементов между минимальным и максимальным элементами '
      f'({array_numbers[min_index]}, {array_numbers[max_index]}) равна {sum_element}')
