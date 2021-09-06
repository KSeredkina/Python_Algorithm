"""2. Посчитать четные и нечетные цифры введенного натурального числа. Например, если введено число 34560,
то у него 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5). """
number = input('Введите натуральное число: ')
even_digit_count = 0
odd_digit_count = 0
if number.isdigit():
    for digit in number:
        i = int(digit)
        if i % 2 == 0:
            even_digit_count += 1
        else:
            odd_digit_count += 1
    print(f'У числа {number} четных цифр - {even_digit_count}, нечетных - {odd_digit_count} ')
else:
    print('Ошибка. Введено не число')
