import sys
input = sys.stdin.readline

n, c = map(int, input().split())
message = list(map(int, input().split()))
number = {}

for i in range(n):
    x = message[i]
    if x in number:
        number[x] += 1
    else:
        number[x] = 1

result = sorted(number.items(), key=lambda x: -x[1])
for x, y in result:
    for _ in range(y):
        print(x, end=' ')