N, M = map(int, input().split()) # N = 수의 개수, M = 구해야 하는 횟수
numbers = list(map(int, input().split())) # N개의 수
sum = [0]
temp = 0

for i in numbers:
    temp += i
    sum.append(temp)

for _ in range(M):
    i, j = map(int, input().split())
    print(sum[j] - sum[i-1])