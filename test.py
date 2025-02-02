n = int(input())

dairy = list(int(input()) for _ in range(n))
dairy.sort(reverse=True)

for i in range(n):
    if i % 3 == 2:
        dairy[i] = 0

print(sum(dairy))