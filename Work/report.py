# report.py
#
# Exercise 2.4
#
# Data/portfolio.csv 파일에는 포트폴리오에 편입된 주식 목록이 있다.
# 연습 문제 1.30에서, 우리는 이 파일을 읽고 간단한 계산을 수행하는 portfolio_cost(filename) 함수를 작성했다.
#
# 코드가 다음과 같을 것이다.

# pcost.py

# import csv
#
# def portfolio_cost(filename):
#     '''포트폴리오 파일의 총 비용(주식수*가격)을 계산'''
#     total_cost = 0.0
#
#     with open(filename, 'rt') as f:
#         rows = csv.reader(f)
#         headers = next(rows)
#         for row in rows:
#             nshares = int(row[1])
#             price = float(row[2])
#             total_cost += nshares * price
#     return total_cost

# 이 코드를 참고해, 새로운 report.py 파일을 생성하라.
# 그 파일에서, 주어진 포트폴리오 파일을 열고 내용을 읽어 튜플의 리스트를 생성하는 read_portfolio(filename) 함수를 정의한다.
# 이를 위해, 위의 코드를 약간 수정해야 한다.


# import csv
#
# def read_portfolio(filename):
#     '''포트폴리오 파일의 총 비용(주식수*가격)을 계산'''
#     portfolio = []
#
#     with open(filename, 'rt') as f:
#         rows = csv.reader(f)
#         headers = next(rows)
#         for row in rows:
#             holding = (row[0], int(row[1]), float(row[2]))
#             portfolio.append(holding)
#     return portfolio

# Exercise 2.5 딕셔너리의 리스트

import csv

def read_portfolio(filename):
    '''포트폴리오 파일의 총 비용(주식수*가격)을 계산'''
    portfolio = []

    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            D = {'name': row[0], 'shares': int(row[1]), 'price': float(row[2])}
            portfolio.append(D)
    return portfolio

def read_prices(filename):
    '''포트폴리오 파일의 총 비용(주식수*가격)을 계산'''
    prices = {}

    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        for row in rows:
            try:
                prices[row[0]] = float(row[1])
            except IndexError:
                pass

    return prices

portfolio = read_portfolio('Data/portfolio.csv')
prices = read_prices('Data/prices.csv')

total_cost = 0.0
for s in portfolio:
    total_cost += s['price'] * s['shares']
total_value = 0.0
for s in portfolio:
    total_value += prices[s['name']] * s['shares']

print('Cost :', total_cost)
print('Value :', total_value - total_cost)

