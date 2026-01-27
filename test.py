import sys
input = sys.stdin.readline

n, m = map(int, input().split())

room = [[0, 0] for _ in range(n + 1)]

for i in range(m):
    k, s, e = map(int, input().split())
    if room[k][1] > s:
        print('NO')
        continue
    room[k][0] = s
    room[k][1] = e
    print('YES')