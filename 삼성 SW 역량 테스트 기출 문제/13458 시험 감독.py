import sys
import math

n = int(sys.stdin.readline().rstrip())
a = list(map(int, sys.stdin.readline().split()))
b, c = map(int, sys.stdin.readline().split())

# 필요한 감독 수
count = 0
for stu in a:
    count += 1
    # 부감독 필요
    if stu - b > 0:
        count += math.ceil((stu-b)/c)

print(count)