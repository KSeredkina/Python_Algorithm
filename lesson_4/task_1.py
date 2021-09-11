"""1. Проанализировать скорость и сложность одного любого алгоритма, разработанных в рамках домашнего задания первых
трех уроков. Примечание: попробуйте написать несколько реализаций алгоритма и сравнить их. Задача из 3 урока. 7. В
одномерном массиве целых чисел определить два наименьших элемента. Они могут быть как равны между собой (оба являться
минимальными), так и различаться. """
import cProfile
import timeit
import random

ELEMENTS_ARRAY = 3000


def generate_array(n: int):
    array = []
    for number in range(n):
        array.append(random.randint(0, 99))
    return array


def min_elements_array_v1(array: []):
    min_index_1 = 0
    min_index_2 = 1
    for i in range(2, len(array)):
        if array[min_index_1] > array[i]:
            min_index_2 = min_index_1
            min_index_1 = i
        elif array[min_index_2] > array[i]:
            min_index_2 = i
    return array[min_index_1], array[min_index_2]


def min_elements_array_v2(array: []):
    sort_array = []
    sort_array.extend(array)
    sort_array.sort()
    return sort_array[0], sort_array[1]


def main():
    array = generate_array(ELEMENTS_ARRAY)
    version_1 = min_elements_array_v1(array)
    version_2 = min_elements_array_v2(array)


cProfile.run('main()')

array_numbers = generate_array(ELEMENTS_ARRAY)

start_time_1 = timeit.default_timer()
min_elements_array_v1(array_numbers)
print(f'Время выполнения 1ого варианта реализации: {timeit.default_timer() - start_time_1}')

start_time_2 = timeit.default_timer()
min_elements_array_v2(array_numbers)
print(f'Время выполнения 2ого варианта реализации: {timeit.default_timer() - start_time_2}')


# Выполнено 3 запуска, каждый последующий шаг с увеличением в 10 раз количества элементов в массиве.
# Генерация случайных чисел линейно: при увеличении шага в 10 раз, время увеличивалось примерно в 10 раз. Сложность
# О(n).
# Вариант с перебором элементов массива: при увеличении шага в 10 раз, время увеличивалось примерно в 10 раз.
# Сложность О(n).
# Вариант с сортировкой: при увеличении шага в 10 раз, время увеличивалось примерно в 10 раз.
# Сложность О(n).
# ВЫВОД:
# Генерация чисел работает медленнее, чем поиск 2х минимальных значений массива. Вариант с перебором
# массива работает незначительно лучше чем вариант с сортировкой. Все функции имеют сложности О(n)

#        18875 function calls in 0.006 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.006    0.006 <string>:1(<module>)
#      3000    0.001    0.000    0.002    0.000 random.py:238(_randbelow_with_getrandbits)
#      3000    0.002    0.000    0.003    0.000 random.py:291(randrange)
#      3000    0.001    0.000    0.004    0.000 random.py:335(randint)
#         1    0.001    0.001    0.006    0.006 task_1.py:11(generate_array)
#         1    0.000    0.000    0.000    0.000 task_1.py:18(min_elements_array_v1)
#         1    0.000    0.000    0.000    0.000 task_1.py:30(min_elements_array_v2)
#         1    0.000    0.000    0.006    0.006 task_1.py:40(main)
#         1    0.000    0.000    0.006    0.006 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#      3000    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#      3000    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#         1    0.000    0.000    0.000    0.000 {method 'extend' of 'list' objects}
#      3865    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}
#         1    0.000    0.000    0.000    0.000 {method 'sort' of 'list' objects}
#
#
# Время выполнения 1ого варианта реализации: 0.00022470000000000823
# Время выполнения 2ого варианта реализации: 0.0002602000000000021
#
# 188394 function calls in 0.067 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.067    0.067 <string>:1(<module>)
#     30000    0.014    0.000    0.020    0.000 random.py:238(_randbelow_with_getrandbits)
#     30000    0.016    0.000    0.036    0.000 random.py:291(randrange)
#     30000    0.009    0.000    0.044    0.000 random.py:335(randint)
#         1    0.012    0.012    0.059    0.059 task_1.py:11(generate_array)
#         1    0.004    0.004    0.004    0.004 task_1.py:18(min_elements_array_v1)
#         1    0.000    0.000    0.004    0.004 task_1.py:30(min_elements_array_v2)
#         1    0.000    0.000    0.067    0.067 task_1.py:40(main)
#         1    0.000    0.000    0.067    0.067 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#     30000    0.003    0.000    0.003    0.000 {method 'append' of 'list' objects}
#     30000    0.003    0.000    0.003    0.000 {method 'bit_length' of 'int' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#         1    0.000    0.000    0.000    0.000 {method 'extend' of 'list' objects}
#     38384    0.004    0.000    0.004    0.000 {method 'getrandbits' of '_random.Random' objects}
#         1    0.004    0.004    0.004    0.004 {method 'sort' of 'list' objects}
#
#
# Время выполнения 1ого варианта реализации: 0.002243099999999998
# Время выполнения 2ого варианта реализации: 0.0027731000000000006
#
# 1883606 function calls in 0.667 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.667    0.667 <string>:1(<module>)
#    300000    0.140    0.000    0.202    0.000 random.py:238(_randbelow_with_getrandbits)
#    300000    0.165    0.000    0.366    0.000 random.py:291(randrange)
#    300000    0.091    0.000    0.457    0.000 random.py:335(randint)
#         1    0.120    0.120    0.610    0.610 task_1.py:11(generate_array)
#         1    0.026    0.026    0.026    0.026 task_1.py:18(min_elements_array_v1)
#         1    0.000    0.000    0.029    0.029 task_1.py:30(min_elements_array_v2)
#         1    0.001    0.001    0.666    0.666 task_1.py:40(main)
#         1    0.000    0.000    0.667    0.667 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#    300000    0.033    0.000    0.033    0.000 {method 'append' of 'list' objects}
#    300000    0.026    0.000    0.026    0.000 {method 'bit_length' of 'int' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#         1    0.001    0.001    0.001    0.001 {method 'extend' of 'list' objects}
#    383596    0.035    0.000    0.035    0.000 {method 'getrandbits' of '_random.Random' objects}
#         1    0.028    0.028    0.028    0.028 {method 'sort' of 'list' objects}
#
#
# Время выполнения 1ого варианта реализации: 0.029344999999999954
# Время выполнения 2ого варианта реализации: 0.030529499999999876
#
# 18841530 function calls in 6.760 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.005    0.005    6.760    6.760 <string>:1(<module>)
#   3000000    1.422    0.000    2.047    0.000 random.py:238(_randbelow_with_getrandbits)
#   3000000    1.702    0.000    3.750    0.000 random.py:291(randrange)
#   3000000    0.882    0.000    4.631    0.000 random.py:335(randint)
#         1    1.181    1.181    6.151    6.151 task_1.py:11(generate_array)
#         1    0.298    0.298    0.298    0.298 task_1.py:18(min_elements_array_v1)
#         1    0.000    0.000    0.300    0.300 task_1.py:30(min_elements_array_v2)
#         1    0.006    0.006    6.755    6.755 task_1.py:40(main)
#         1    0.000    0.000    6.760    6.760 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#   3000000    0.338    0.000    0.338    0.000 {method 'append' of 'list' objects}
#   3000000    0.269    0.000    0.269    0.000 {method 'bit_length' of 'int' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#         1    0.007    0.007    0.007    0.007 {method 'extend' of 'list' objects}
#   3841520    0.356    0.000    0.356    0.000 {method 'getrandbits' of '_random.Random' objects}
#         1    0.293    0.293    0.293    0.293 {method 'sort' of 'list' objects}
#
#
# Время выполнения 1ого варианта реализации: 0.30436710000000033
# Время выполнения 2ого варианта реализации: 0.3095733000000003
