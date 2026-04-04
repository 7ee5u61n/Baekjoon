w = int(input())

s = 2
for i in range(2, 10000):
    if (w*2) // i == i:
        s = i
        break

print(s*4)