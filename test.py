N = int(input())

A = []
for _ in range(N):
    A.append(int(input()))

M = int(input())

price = 0
for _ in range(M):
    B = int(input())-1
    price += A[B]

print(price)