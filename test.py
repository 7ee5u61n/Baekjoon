n = int(input())

result = 0
for i in range(1, 501):
    for j in range(i, 501):
        if i**2 + n == j**2:
            result += 1

print(result)