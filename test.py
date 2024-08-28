time = 0
for _ in range(4):
    time += (int(input()))

minute = time // 60
second = time % 60

print(minute)
print(second)