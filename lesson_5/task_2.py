"""2. Написать программу сложения и умножения двух шестнадцатеричных чисел. При этом каждое число представляется как
массив, элементы которого это цифры числа. Например, пользователь ввёл A2 и C4F. Сохранить их как [‘A’, ‘2’] и [‘C’,
‘4’, ‘F’] соответственно. Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’,
‘E’]. Примечание: для решения задач попробуйте применить какую-нибудь коллекцию из модуля collections """
from collections import deque

HEX_NUM = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
           'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15,
           0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9',
           10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}


def sum_hex(num_1, num_2):
    result = deque()
    add_digit = 0
    if len(num_2) > len(num_1):
        num_1, num_2 = deque(num_2), deque(num_1)
    else:
        num_1, num_2 = deque(num_1), deque(num_2)
    while num_1:
        if num_2:
            res = HEX_NUM[num_1.pop()] + HEX_NUM[num_2.pop()] + add_digit
        else:
            res = HEX_NUM[num_1.pop()] + add_digit
        add_digit = 0
        if res < 16:
            result.appendleft(HEX_NUM[res])
        else:
            result.appendleft(HEX_NUM[res - 16])
            add_digit = 1
    if add_digit:
        result.appendleft('1')
    return list(result)


def multiply_hex(num_1, num_2):
    result = deque()
    mult_digit_num = deque([deque() for _ in range(len(num_2))])
    num_1, num_2 = num_1.copy(), deque(num_2)
    for i in range(len(num_2)):
        digit_num_2 = HEX_NUM[num_2.pop()]
        for j in range(len(num_1) - 1, -1, -1):
            mult_digit_num[i].appendleft(digit_num_2 * HEX_NUM[num_1[j]])
        for _ in range(i):
            mult_digit_num[i].append(0)
    add_digit = 0
    for _ in range(len(mult_digit_num[-1])):
        res = add_digit
        for i in range(len(mult_digit_num)):
            if mult_digit_num[i]:
                res += mult_digit_num[i].pop()
        if res < 16:
            result.appendleft(HEX_NUM[res])
        else:
            result.appendleft(HEX_NUM[res % 16])
            add_digit = res // 16
    if add_digit:
        result.appendleft(HEX_NUM[add_digit])
    return list(result)


number_1 = list(input('Введите 1ое шестнадцатеричное число: ').upper())
number_2 = list(input('Введите 2ое шестнадцатеричное число: ').upper())

print(number_1, '+', number_2, '=', sum_hex(number_1, number_2))
print(number_1, '*', number_2, '=', multiply_hex(number_1, number_2))
