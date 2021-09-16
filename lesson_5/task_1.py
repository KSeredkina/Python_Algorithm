"""1. Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартала (т.е. 4 отдельных
числа) для каждого предприятия. Программа должна определить среднюю прибыль (за год для всех предприятий) и вывести
наименования предприятий, чья прибыль выше среднего и отдельно вывести наименования предприятий, чья прибыль ниже
среднего. """
from collections import namedtuple

Enterprise = namedtuple('Enterprise', ['name', 'profit_q1', 'profit_q2', 'profit_q3', 'profit_q4', 'profit_year'])

count_enterprises = int(input('Введите количество предприятий: '))
enterprises = [0 for _ in range(count_enterprises)]
total_profit_sum = 0

for i in range(count_enterprises):
    name = input('Введите наименование предприятия ' + str(i + 1) + ': ')
    q1 = float(input('Введите прибыль 1ого квартала: '))
    q2 = float(input('Введите прибыль 2ого квартала: '))
    q3 = float(input('Введите прибыль 3ого квартала: '))
    q4 = float(input('Введите прибыль 4ого квартала: '))
    profit_year = q1 + q2 + q3 + q4
    total_profit_sum += profit_year
    enterprises[i] = Enterprise(
        name=name,
        profit_q1=q1,
        profit_q2=q2,
        profit_q3=q3,
        profit_q4=q4,
        profit_year=profit_year
    )

if count_enterprises == 1:
    print(f'Для анализа передано 1 предприятие: {enterprises[0].name} {enterprises[0].profit_year}')
else:
    total_profit_average = total_profit_sum / count_enterprises

    print(f'Средняя прибыль между предприятиями: {total_profit_average: 2f}')
    for enterprise in enterprises:
        if enterprise.profit_year < total_profit_average:
            print(f'Предприятие c прибылью меньше средней: {enterprise.name} {enterprise.profit_year}')
        elif enterprise.profit_year > total_profit_average:
            print(f'Предприятие с прибылью больше средней: {enterprise.name} {enterprise.profit_year}')
