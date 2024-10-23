# 남은 퇴사일
n = int(input())
t = [0]*(n)
p = [0]*(n)

# 상담 시간, 금액
for i in range(n):
    t[i], p[i] = map(int, input().split())

d = [0]*(n+1)

for i in range(n-1, -1, -1):
    if i+t[i] <= n:
        d[i] = max(d[i+1], d[i+t[i]]+p[i])
    else:
        d[i]=d[i+1]

print(d[0])