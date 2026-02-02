a, d, k = map(int, input().split())

for i in range(1, int(1e6)+2):
    if a == k:
        print(i)
        break
    a += d
if a != k:
    print('X')