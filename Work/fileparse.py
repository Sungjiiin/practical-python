# fileparse.py
#
# Exercise 3.3
import csv

def parse_csv(filename, select=None, types=None, has_headers=True, delimiter=','):
    '''
    CSV 파일을 파싱해 레코드의 목록을 생성
    '''
    with open(filename) as f:
        rows = csv.reader(f, delimiter=delimiter)

        # 헤더를 읽음
        if has_headers:
            headers = next(rows)
        else:
            headers = []

        if select:
            indices = [headers.index(col) for col in select]
            headers = select
        else:
            indices = []

        records = []
        for row in rows:
            if not row:    # 데이터가 없는 행을 건너뜀
                continue
            if indices:
                row = [row[index] for index in indices]
            if types:
                row = [func(val) for func, val in zip(types, row)]
            if headers:
                record = dict(zip(headers, row))
            else:
                record = tuple(row)
            records.append(record)

    return records