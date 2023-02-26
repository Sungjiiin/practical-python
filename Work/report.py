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
# Exercise 2.16
#
# import csv

# def read_portfolio(filename):
#     '''포트폴리오 파일의 총 비용(주식수*가격)을 계산'''
#     portfolio = []
#
#     with open(filename, 'rt') as f:
#         rows = csv.reader(f)
#         headers = next(rows)
#         for row in rows:
#             record = dict(zip(headers, row))
#             stock = {
#                 'name': record['name'],
#                 'shares': int(record['shares']),
#                 'price': float(record['price'])
#             }
#             portfolio.append(stock)
#     return portfolio
#
# def read_prices(filename):
#     '''포트폴리오 파일의 총 비용(주식수*가격)을 계산'''
#     prices = {}
#
#     with open(filename, 'rt') as f:
#         rows = csv.reader(f)
#         for row in rows:
#             try:
#                 prices[row[0]] = float(row[1])
#             except IndexError:
#                 pass
#
#     return prices

# portfolio = read_portfolio('Data/portfolio.csv')
# prices = read_prices('Data/prices.csv')

# total_cost = 0.0
# for s in portfolio:
#     total_cost += s['price'] * s['shares']
# total_value = 0.0
# for s in portfolio:
#     total_value += prices[s['name']] * s['shares']
#
# print('Cost :', total_cost)
# print('Value :', total_value - total_cost)

# Exercise 2.9 데이터 수집하기

# def make_report(portfolio, prices):
#     report = []
#
#     for s in portfolio:
#         temp = (s['name'], s['shares'], s['price'], s['price']-prices[s['name']])
#         report.append(temp)
#     return report
#
# portfolio = read_portfolio('Data/portfolio.csv')
# prices = read_prices('Data/prices.csv')
# report = make_report(portfolio, prices)
#
# # Exercise 2.11, 12 : 헤더 추가하기
# headers = ('Name', 'Shares', 'Price', 'Change')
#
# print('%10s %10s %10s %10s' % headers)
# print(('-' * 10 + ' ') * len(headers))
# for r in report:
#     print('%10s %10d %10.2f %10.2f' % r)
#
# print('%10s %10s %10s %10s' % headers)
# print(('-' * 10 + ' ') * len(headers))
# for name, shares, price, change in report:
#     print(f'{name:>10s} {shares:>10d} {price:>10.2f} {change:>10.2f}')

# Exercise 3.1 : 프로그램을 함수의 컬렉션을 구조화하기

# def print_report(report):
#     headers = ('Name', 'Shares', 'Price', 'Change')
#
#     print('%10s %10s %10s %10s' % headers)
#     print(('-' * 10 + ' ') * len(headers))
#     for r in report:
#         print('%10s %10d %10.2f %10.2f' % r)
#
# def portfolio_report(portfolio_filename, prices_filename):
#
#     portfolio = read_portfolio(portfolio_filename)
#     prices = read_prices(prices_filename)
#
#     report = make_report(portfolio=portfolio, prices=prices)
#     print_report(report)

#portfolio_report('Data/portfolio.csv', 'Data/prices.csv')

# interactive에서 실행하면 다른 파일도 가져와서 출력 가능
# >>> for name in files:     }')           v')
# ...     print(f'{name:-^43s}')
# ...     report.portfolio_report(name, 'Data/prices.csv')
# ...     print()

# Exercise 3.12

from fileparse import parse_csv

def read_portfolio(filename):
    '''포트폴리오 파일의 총 비용(주식수*가격)을 계산'''
    return parse_csv(filename, select=['name','shares','price'], types=[str,int,float])

def read_prices(filename):
    '''포트폴리오 파일의 총 비용(주식수*가격)을 계산'''
    return dict(parse_csv(filename, types=[str,float], has_headers=False))

def make_report(portfolio, prices):
    report = []

    for s in portfolio:
        temp = (s['name'], s['shares'], s['price'], s['price']-prices[s['name']])
        report.append(temp)
    return report


def print_report(report):
    headers = ('Name', 'Shares', 'Price', 'Change')

    print('%10s %10s %10s %10s' % headers)
    print(('-' * 10 + ' ') * len(headers))
    for r in report:
        print('%10s %10d %10.2f %10.2f' % r)

def portfolio_report(portfolio_filename, prices_filename):

    portfolio = read_portfolio(portfolio_filename)
    prices = read_prices(prices_filename)

    report = make_report(portfolio=portfolio, prices=prices)
    print_report(report)

def main(argv):
    portfolio_report(*argv[1:])

if __name__ == "__main__":
    import sys
    main(sys.argv)