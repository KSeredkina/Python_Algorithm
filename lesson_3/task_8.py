"""8. Матрица 5x4 заполняется вводом с клавиатуры кроме последних элементов строк. Программа должна вычислять сумму
введенных элементов каждой строки и записывать ее в последнюю ячейку строки. В конце следует вывести полученную
матрицу. """

matrix = []

for m in range(4):
    matrix.append([])
    sum_row = 0
    for n in range(4):
        user_number = int(input(f'Введите элемент {m+1} строки и {n+1} столбца: '))
        sum_row += user_number
        matrix[m].append(user_number)
    matrix[m].append(sum_row)

for element in matrix:
    print(element)
