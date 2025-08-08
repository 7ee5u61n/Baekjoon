n = int(input())

result = 0
for i in range(n):
    arr = list(map(int, input().split()))
    result += sum(arr)

print(result)