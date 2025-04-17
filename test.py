today = list(map(int, input().split('-')))
n = int(input())

usable = 0
for _ in range(n):
    expire = list(map(int, input().split('-')))
    if today[0] < expire[0]:
        usable += 1
        continue
    elif today[0] == expire[0]:
        if today[1] < expire[1]:
            usable += 1
            continue
        elif today[1] == expire[1]:
            if today[2] <= expire[2]:
                usable += 1
                continue

print(usable)