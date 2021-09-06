"""4. Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...Количество элементов (n) вводится с
клавиатуры. """

count_elements_range = int(input('Введите количество элементов ряда: '))
i = 0
range_element = 1
sum_elements = 0
while i < count_elements_range:
    sum_elements += range_element
    range_element /= -2
    i += 1
print(f'Сумма из {count_elements_range} элементов ряда равна {sum_elements}')
