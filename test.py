import sys
input = sys.stdin.readline

n = int(input())

student = []
result = 100000
count = 0

for _ in range(n):
    info = list(map(int, input().split()))
    if info[0] == 1:
        student.append(info[1])
    else:
        student.pop(0)

    if len(student) > count:
        count = len(student)
        result = student[-1]
    elif len(student) == count:
        result = min(student[-1], result)

print(count, result)