import sys

N, M = map(int, input().split()) # A와 B 원소의 개수

A = set(map(int, input().split()))
B = set(map(int, input().split()))

A_B = list(A - B)
B_A = list(B - A)

print(len(A_B + B_A))