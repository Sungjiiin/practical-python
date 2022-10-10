# 1.2 첫 번째 프로그램
#
# 다음 문제를 풀어 보자.
#
# 어느 날 아침, 당신은 시카고의 시어스 타워(Sears tower) 근처를 거닐다가 보도에 1 달러 지폐를 한 장 올려뒀다.
# 그 후 매일 외출할 때마다 그 위에 지폐를 얹어 탑을 쌓으며, 높이는 매일 두 배로 불어난다.
# 돈으로 쌓은 탑의 높이가 시어스 타워의 높이와 같아지려면 시간이 얼마나 걸릴까?

bill_thickness = 0.11 * 0.001
sears_height = 442
num_bills = 1
day = 1

while num_bills * bill_thickness < sears_height:
    print(day, num_bills, num_bills * bill_thickness)
    day = day + 1
    num_bills = num_bills * 2 # 다음 세 문장은 들여쓰기가 같으므로 함께 묶여 반복적으로 수행된다.

print('Number of days', day)
print('Number of bills', num_bills)
print('Final_height', num_bills * bill_thickness)

# Best practice Indentation
# - Not Tab, use space
# - Use 4 space per levels
# - Use a Python-aware editor.

# 같은 블록 내의 들여쓰기에 대해서만 일관적인 들여쓰기를 요구한다. 다음 코드는 오류를 일으킨다
# '''
# while num_bills * bill_thickness < sears_height:
#     print(day, num_bills, num_bills * bill_thickness)
#         day = day + 1  # 오류
#     num_bills = num_bills * 2
# '''