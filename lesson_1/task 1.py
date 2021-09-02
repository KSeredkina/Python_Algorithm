# 1. Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.

number = int(input("Введите трехзначное число: "))

if number // 100 != 0 and number // 1000 == 0:
    units = number % 10
    tens = number % 100 // 10
    hundreds = number // 100
    sum_digits = units + tens + hundreds
    product_digits = units * tens * hundreds
    print(f'Сумма цифр числа: {sum_digits}')
    print(f'Произведение цифр числа: {product_digits}')
else:
    print('Ошибка. Введено не трехзначное число')
