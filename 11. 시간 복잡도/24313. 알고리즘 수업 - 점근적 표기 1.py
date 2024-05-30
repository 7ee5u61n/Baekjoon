a1, a0 = map(int, input().split())
c = int(input())
n0 = int(input())

answer = 0
for i in range(n0, 101):
    if a1 * i + a0 > c * i:
        answer = 0
        break
    else:
        answer = 1

print(answer)