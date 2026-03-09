n = int(input())
student = list(map(int, input().split()))

line = [x for x in range(1, n+1)]
result = 0
for i in range(n):
    if student[i] != line[i]:
        result += 1

print(result)