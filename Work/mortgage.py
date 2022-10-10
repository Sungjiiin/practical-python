# mortgage.py
#
# Exercise 1.7

principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
# while principal > 0:
#     principal = principal * (1+rate/12) - payment
#     total_paid = total_paid + payment
#
# print('Total paid', total_paid)

# Exercise 1.8

# added_payment = 1000.0
# added_month = 12
# paid_month = 0

# while principal > 0:
#     if added_month > 0:
#         principal = principal * (1 + rate / 12) - (added_payment + payment)
#         added_month -= 1
#         total_paid = total_paid + (added_payment + payment)
#     else:
#         principal = principal * (1+rate/12) - payment
#         total_paid = total_paid + payment
#     paid_month += 1
#
# print('Total paid', total_paid)
# print('Paid month', paid_month)

# Exercise 1.9

# paid_month = 0
# extra_payment_start_month = 61
# extra_payment_end_month = 108
# extra_payment = 1000
#
# while principal > 0:
#     if extra_payment_start_month <= paid_month <= extra_payment_end_month:
#         principal = principal * (1 + rate / 12) - (extra_payment + payment)
#         total_paid = total_paid + (extra_payment + payment)
#     else:
#         principal = principal * (1+rate/12) - payment
#         total_paid = total_paid + payment
#     paid_month += 1
#     print(paid_month, round(total_paid, 2), round(principal, 2))
#
# print('Total paid', total_paid)
# print('Paid month', paid_month)

# Exercise 1.10

paid_month = 0
extra_payment_start_month = 61
extra_payment_end_month = 108
extra_payment = 1000

while principal > 0:
    principal = principal * (1 + rate / 12) - payment
    total_paid = total_paid + payment
    if extra_payment_start_month <= paid_month <= extra_payment_end_month:
        principal -= extra_payment
        total_paid = total_paid + extra_payment

    if principal < 0:
        break
    paid_month += 1
    print(f'{paid_month} ${total_paid:0.2f} ${principal:0.2f}')

# Exercise 1.17
print(f'Total paid ${total_paid:0.2f}')
print(f'Paid month ${paid_month}')