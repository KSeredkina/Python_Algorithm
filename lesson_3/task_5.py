"""5. В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве."""
import random

array_numbers = []
for number in range(10):
    array_numbers.append(random.randint(-99, 99))
print(f'Заданный массив: {array_numbers}')

index = -1

for i in range(len(array_numbers)):
    if array_numbers[i] < 0 and index == -1:
        index = i
    elif 0 > array_numbers[i] > array_numbers[index]:
        index = i

if index == -1:
    print(f'В массиве нет отрицательных элементов')
else:
    print(f'В массиве максимальный отрицательный элемент: {array_numbers[index]}, на позиции {index}')
