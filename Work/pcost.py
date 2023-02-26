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

# import csv
# import sys
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
# if len(sys.argv) == 2:
#     filename = sys.argv[1] # 명령행에서 전달받은 인자가 있을 경우 sys.argv 리스트에 들어있다.
# else:
#     filename = 'Data/portfolio.csv'
#
# cost = portfolio_cost(filename)
# print(f'Total cost: {cost}')

# Exercise 2.15, 16 : 실용적인 enumerate() 예제

# 주식 포트폴리오 데이터가 있는 Data/missing.csv의 일부 행에는 데이터가 누락되어 있다.
# enumerate()를 사용해 pcost.py 프로그램이 잘못된 입력을 만나면 행 번호와 경고 메시지를 프린트하게 해 보라.


# import csv
# import sys
#
# def portfolio_cost(filename):
#     filename: str
#
#     total_cost = 0
#     f = open(filename)
#     rows = csv.reader(f)
#     headers = next(rows)
#     for idx, row in enumerate(rows, start=1):
#         record = dict(zip(headers, row))
#         try:
#             nshares = int(record['shares'])
#             price = float(record['price'])
#             total_cost += nshares * price
#         except ValueError:
#             print(f'Row {idx}: Bad row: {row}')
#
#     return total_cost
#
# if len(sys.argv) == 2:
#     filename = sys.argv[1] # 명령행에서 전달받은 인자가 있을 경우 sys.argv 리스트에 들어있다.
# else:
#     filename = 'Data/portfolio.csv'
#
# cost = portfolio_cost(filename)
# print(f'Total cost: {cost}')

# 데이터 파일이 앞에서 사용한 것과 완전히 달라지더라도 프로그램이 여전히 작동할 것이다. 멋지지 않은가!
#
# 코드를 많이 바꾸지 않았지만 그 효과는 상당하다. 
# 새로운 버전의 portfolio_cost() 함수에서는 고정된 파일 형식을 하드코딩하는 대신,
# 어느 CSV 파일이 들어오더라도 원하는 값을 골라낼 수 있게 됐다.
# 필요한 컬럼이 파일에 있기만 하면 코드는 잘 작동한다.


# Exercise 3.14

import report

def portfolio_cost(filename):
    filename: str

    total_cost = 0
    portfolio = report.read_portfolio(filename)

    for idx, row in enumerate(portfolio):
        try:
            nshares = int(row['shares'])
            price = float(row['price'])
            total_cost += nshares * price
        except ValueError:
            print(f'Row {idx}: Bad row: {row}')

    return total_cost

def main(argv):
    print(f'Total cost: {portfolio_cost(*argv[1:])}')

if __name__ == "__main__":
    import sys
    main(sys.argv)