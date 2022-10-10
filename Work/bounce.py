# bounce.py
#
# Exercise 1.5

ball_height = 100
i = 0

while i < 10:
    ball_height *= 3/5
    i += 1
    print(i, round(ball_height, 4))