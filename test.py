n = int(input())
T = 0
B = 5000
for _ in range(n):
    t, b = map(int, input().split())
    T = max(t, T)
    B = min(b, B)

print((T*B)%7+1)
