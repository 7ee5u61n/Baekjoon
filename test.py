n = int(input())
arr = list(map(int, input().split()))
arr.sort()

prime = 10000
least = 20000*10000
for i in range(n):
    sm = 0
    for j in range(n):
        sm += abs(arr[i]-arr[j])
    if sm < least:
        least = sm
        prime = arr[i]

print(prime)