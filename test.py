n = int(input())
arr = list(map(int, input().split()))

result = 0
for i in range(len(arr)):
    if arr[i] == n:
        result += 1

print(result)