import sys
input = sys.stdin.readline

n, k = map(int, input().split())

fk = k % 10
fk2 = (k*2) % 10

arr = []
for i in range(1, n + 1):
    if i % 10 != fk and i % 10 != fk2:
        arr.append(i)

print(len(arr))
print(*arr)