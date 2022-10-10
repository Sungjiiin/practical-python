# sears.py

bill_thickness = 0.11 * 0.001    # 미터(0.11 mm)
sears_height   = 442             # 높이(미터)
num_bills      = 1
day            = 1

while num_bills * bill_thickness < sears_height:
    print(day, num_bills, num_bills * bill_thickness)
    day = day + 1
    num_bills = num_bills * 2

print('Number of days', day)
print('Number of bills', num_bills)
print('Final height', num_bills * bill_thickness)

# Traceback (most recent call last):
#   File ".\sears.py", line 10, in <module>
#     day = days + 1
# NameError: name 'days' is not defined

# -> 오류 메시지를 읽는건 매우 중요하다. 프로그램 충돌시 traceback 메시지에서 마지막 행을 읽으면 충돌 이유를 알 수 있다.
# 코드의 몇 번째 행에 오류가 있는가? -> 10번째 행에 오류가 있다
# 무엇이 잘못되었는가? -> name 'days'는 정의되지 않은 이름이다. 이전에 정의한 'day'로 변경해야한다
# 오류를 수정하라
# 프로그램을 성공적으로 실행하라