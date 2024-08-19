import sys

Sum = 0
for i in range(5):
    point = list(map(int, input().split()))
    if sum(point) > Sum:
        Sum = sum(point)
        winner = i+1

print(winner, Sum)