n = int(input())
count = 0
while True:
    if len(str(n*2)) > len(str(n)):
        break

    n *= 2
    count += 1

print(count)