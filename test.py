date = list(map(int, input().split('-')))
n = int(input())

for i in range(n):
    date[2] += 1
    if date[2] > 30:
        date[2] = 1
        date[1] += 1
        if date[1] > 12:
            date[1] = 1
            date[0] += 1

print(f"{date[0]:04d}-{date[1]:02d}-{date[2]:02d}")