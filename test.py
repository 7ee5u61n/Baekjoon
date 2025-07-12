s = int(input())

sm = 0
n = 0

while True:
    n += 1
    sm += n
    if sm > s:
        n -= 1
        break

print(n)