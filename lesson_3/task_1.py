"""1. В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому из чисел в диапазоне от 2 до
9. """
multiples_result = {}
for number in range(2, 10):
    multiples_result[number] = []
    for number_range in range(2, 100):
        if number_range % number == 0:
            multiples_result[number].append(number_range)
    print(f'Для числа {number} кратны - {len(multiples_result[number])} чисел.')
