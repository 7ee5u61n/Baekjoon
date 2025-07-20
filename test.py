n = int(input())
arr = list(map(int, input().split()))

result = (90*(n-1)-sum(arr))*2

print(result)