n = int(input())

result = 0
for i in range(n):
    x = input().split('-')
    if int(x[1]) <= 90:
        result += 1

print(result)