"""6. В программе генерируется случайное целое число от 0 до 100. Пользователь должен его отгадать не более чем за 10
попыток. После каждой неудачной попытки должно сообщаться больше или меньше введенное пользователем число, чем то,
что загадано. Если за 10 попыток число не отгадано, то вывести загаданное число. """
import random

random_number = random.randint(0, 100)
# print(random_number)
trying = 1
while trying <= 10:
    print(f'{trying} попытка из 10')
    user_number = int(input('Введите число от 1 до 100: '))
    if user_number == random_number:
        print('Число угадано')
        break
    elif user_number > random_number:
        print(f'Ваше число {user_number} больше загаданного')
    else:
        print(f'Ваше число {user_number} меньше загаданного')
    trying += 1
else:
    print(f'Попытки исчерпаны. Загаданное число - {random_number}')
