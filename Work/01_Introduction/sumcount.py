def sumcount(n):
    '''
    정수 1부터 n까지의 합을 반환
    '''
    total = 0
    while n > 0:
        total += n
        n -= 1
    return total


a = sumcount(100)
print(a)