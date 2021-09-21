"""1. Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах в рамках первых трех
уроков. Проанализировать результат и определить программы с наиболее эффективным использованием памяти. Примечание:
Для анализа возьмите любые 1-3 ваших программы или несколько вариантов кода для одной и той же задачи. Результаты
анализа вставьте в виде комментариев к коду. Также укажите в комментариях версию Python и разрядность вашей ОС. """
# Параметры АРМ: Windows x64, Intel i5 12Gb, Python 3.9.2
import sys
from random import random

# Задание 9ое  3ого урока. Затраты памяти программой составляют: 1040 байт. Каждый переменная - объект,  чем больше
# переменных используется в коде (временных), тем больше потребляется памяти. Тип данных "список" позволяет облегчить
# обращение к элементам и сэкономить память, если размер хранимых данных будет являться значительным,
# так как добавление нового элемента в список добавляет новую ссылку, которая значительно меньше занимает памяти
# нежели отдельно хранимая переменная.

n = 5
m = 4
matrix = []
for i in range(n):
    row_matrix = []
    for j in range(m):
        row_matrix.append(int(random() * 256))
    matrix.append(row_matrix)
# print('Матрица:')
# for i in matrix:
# print(i)
# print('---------')
for j in range(m):
    max_among_min = matrix[0][j]
    for i in range(n):
        if matrix[i][j] > max_among_min:
            max_among_min = matrix[i][j]
    # print(f'Максимальный элемент столбца {j} - {max_among_min}')

sum_size = 0

sum_size += sys.getsizeof(n)*2
sum_size += sys.getsizeof(m)*2
sum_size += sys.getsizeof(i)*2
sum_size += sys.getsizeof(j)*2
sum_size += sys.getsizeof(matrix)
for elm_row in matrix:
    sum_size += sys.getsizeof(elm_row)
sum_size += sys.getsizeof(row_matrix)
for elm_row in row_matrix:
    sum_size += sys.getsizeof(elm_row)
sum_size += sys.getsizeof(max_among_min)*2

print(f'Затраты памяти программой составляют: {sum_size} байт')
