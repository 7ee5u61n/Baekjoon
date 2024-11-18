count = 0
for i in range(8):
    chess = list(input())
    if i % 2 == 0:
        for j in range(0, 7, 2):
            if chess[j] == 'F':
                count += 1
    else:
        for j in range(1, 8, 2):
            if chess[j] == 'F':
                count += 1

print(count)