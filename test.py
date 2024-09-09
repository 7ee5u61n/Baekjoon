A, B, C = map(int, input().split())
I, J, K = map(int, input().split())

R = min(A/I, B/J, C/K)

A1 = A-I*R
B1 = B-J*R
C1 = C-K*R

if A1 == int(A1):
    A2 = (int(A1))
else:
    A2 = format(A1, '6f')

if B1 == int(B1):
    B2 = int(B1)
else:
    B2 = format(B1, '6f')

if C1 == int(C1):
    C2 = int(C1)
else:
    C2 = format(C1, '6f')

print(A2, B2, C2)