import sys
input = sys.stdin.readline

n = int(input())
entered = set()
count = 0
for _ in range(n):
    a, b = map(int, input().split())
    if b == 1:
        if a in entered:
            count += 1
        else:
            entered.add(a)
    else:
        if a in entered:
            entered.remove(a)
        else:
            count += 1

print(count + len(entered))