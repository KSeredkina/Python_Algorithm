"""9. Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр. Вывести на экран это число и
сумму его цифр. """

list_number = map(int, input('Введите натуральные числа: ').split())
max_number = 0
max_sum = 0
for number in list_number:
    max_num = number
    sum_num = 0
    while number > 0:
        sum_num += number % 10
        number //= 10
    if sum_num > max_sum:
        max_sum = sum_num
        max_number = max_num
print(f'У числа {max_number} наибольшая сумма цифр - {max_sum}')
