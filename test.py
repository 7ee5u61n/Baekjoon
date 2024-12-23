n = int(input())
changyeong = 100
sangdeok = 100

for _ in range(n):
    a, b = map(int, input().split())
    if a < b:
        changyeong -= b
    elif a > b:
        sangdeok -= a

print(changyeong)
print(sangdeok)