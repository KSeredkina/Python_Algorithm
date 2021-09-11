"""2. Написать два алгоритма нахождения i-го по счёту простого числа. Без использования «Решета Эратосфена»;
Используя алгоритм «Решето Эратосфена». Примечание ко всему домашнему заданию: Проанализировать скорость и сложность
алгоритмов. Результаты анализа сохранить в виде комментариев в файле с кодом. """
import timeit

NUMBER_EXECUTIONS = 1
COUNT_NUMBER = 1000


def prime_numbers(num: int):
    array_prime_numbers = []
    for i in range(2, num + 1):
        for j in array_prime_numbers:
            if i % j == 0:
                break
        else:
            array_prime_numbers.append(i)
    return array_prime_numbers


def prime_numbers_eratosthenes(num: int):
    array_numbers = []
    for i in range(num + 1):
        array_numbers.append(i)
    array_numbers[1] = 0
    array_primes = []

    i = 2
    while i <= num:
        if array_numbers[i] != 0:
            array_primes.append(array_numbers[i])
            for j in range(i, num + 1, i):
                array_numbers[j] = 0
        i += 1
    return array_primes


time_1 = timeit.timeit(f'prime_numbers({COUNT_NUMBER})',
                       setup='from __main__ import prime_numbers',
                       number=NUMBER_EXECUTIONS)

time_2 = timeit.timeit(f'prime_numbers_eratosthenes({COUNT_NUMBER})',
                       setup='from __main__ import prime_numbers_eratosthenes',
                       number=NUMBER_EXECUTIONS)

print(f'Время выполнения алгоритма поиска простых чисел без использования алгоритма "Решето Эратосфена" - {time_1}')
print(f'Время выполнения алгоритма "Решето Эратосфена" по поиску простых чисел - {time_2}')
print(f'Алгоритм "Решето Эратосфена" быстрее в {round(time_1 / time_2, 0)} раз')

# Сложность алгоритма поиска простых чисел без использования алгоритма "Решето Эратосфена" - О(n^2)
# Сложность алгоритма "Решето Эратосфена" - O(n)


# Изменение времени при увеличения шага в 10 раз каждую итерацию: Время выполнения алгоритма поиска простых чисел без
# Время использования алгоритма "Решето Эратосфена" - 0.0005357999999999995
# Время выполнения алгоритма "Решето Эратосфена" по поиску простых чисел - 0.00024089999999999875

# Время выполнения алгоритма поиска простых чисел без использования алгоритма "Решето Эратосфена" - 0.0313677
# Время выполнения алгоритма "Решето Эратосфена" по поиску простых чисел - 0.0023734999999999937

# Время выполнения алгоритма поиска простых чисел без использования алгоритма "Решето Эратосфена" - 2.0284168
# Время выполнения алгоритма "Решето Эратосфена" по поиску простых чисел - 0.028904199999999935
