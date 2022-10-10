# pcost.py
#
# Exercise 1.27

# total_cost = 0
#
# with open('Data/portfolio.csv', 'rt') as f:
#     headers = next(f)
#     for line in f:
#         row = line.split(',')
#         num, price = int(row[1]), float(row[2])
#         total_cost += num * price
#
# print(f'Total cost {total_cost}')

# Exercise 1.30

# def portfolio_cost(filename):
#     total_cost = 0
#     with open(filename, 'rt') as f:
#         headers = next(f)
#         for line in f:
#             row = line.split(',')
#             if row[1] == '' or row[2] == '':
#                 pass
#             else:
#                 num, price = int(row[1]), float(row[2])
#                 total_cost += num * price
#
#     return total_cost
#
# cost = portfolio_cost('Data/portfolio.csv')
# print(f'Total cost: {cost}')

# Exercise 1.32 : Use library function

# import csv
#
# def portfolio_cost(filename):
#     total_cost = 0
#     f = open(filename)
#     rows = csv.reader(f)
#     headers = next(rows)
#     for row in rows:
#         if row[1] == '' or row[2] == '':
#             pass
#         else:
#             num, price = int(row[1]), float(row[2])
#             total_cost += num * price
#
#     return total_cost
#
# cost = portfolio_cost('Data/portfolio.csv')
# print(f'Total cost: {cost}')

# Exercise 1.33 : Read script at command line
# 실제 프로그램에서는 인자를 직접 넣어주는 형태로 만드는게 좋다

import csv
import sys

def portfolio_cost(filename):
    total_cost = 0
    f = open(filename)
    rows = csv.reader(f)
    headers = next(rows)
    for row in rows:
        if row[1] == '' or row[2] == '':
            pass
        else:
            num, price = int(row[1]), float(row[2])
            total_cost += num * price

    return total_cost

if len(sys.argv) == 2:
    filename = sys.argv[1] # 명령행에서 전달받은 인자가 있을 경우 sys.argv 리스트에 들어있다.
else:
    filename = 'Data/portfolio.csv'

cost = portfolio_cost(filename)
print(f'Total cost: {cost}')