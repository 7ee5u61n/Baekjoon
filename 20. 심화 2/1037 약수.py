import sys

amount = int(sys.stdin.readline()) # 진짜 약수의 개수
tureDivisor = set(map(int, sys.stdin.readline().split())) # 진짜 약수

print(min(tureDivisor) * max(tureDivisor))