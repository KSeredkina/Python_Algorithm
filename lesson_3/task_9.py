"""9. Найти максимальный элемент среди минимальных элементов столбцов матрицы."""
from random import random

n = 5
m = 4
matrix = []
for i in range(n):
    row_matrix = []
    for j in range(m):
        row_matrix.append(int(random() * 256))
    matrix.append(row_matrix)
print('Матрица:')
for i in matrix:
    print(i)
print('---------')
for j in range(m):
    max_among_min = matrix[0][j]
    for i in range(n):
        if matrix[i][j] > max_among_min:
            max_among_min = matrix[i][j]
    print(f'Максимальный элемент столбца {j} - {max_among_min}')
