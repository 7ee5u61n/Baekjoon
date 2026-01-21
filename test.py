p = list(map(int, input().split()))
x, y, r = map(int, input().split())

result = 0
for i in range(len(p)):
    if p[i] == x:
        result = i+1
        break

print(result)