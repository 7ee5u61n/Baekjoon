n = int(input())
v = list(map(int, input().split()))

start = v.index(max(v))+1

result = 0
for i in range(n-1):
    result += v[(i+start)%n]

print(result)