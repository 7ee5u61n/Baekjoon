import math

L = int(input())
A = int(input())
B = int(input())
C = int(input())
D = int(input())

korean = math.ceil(A / C)
mathematics = math.ceil(B / D)

if korean >= mathematics:
    homeworkDay = korean
else:
    homeworkDay = mathematics

print(L - homeworkDay)