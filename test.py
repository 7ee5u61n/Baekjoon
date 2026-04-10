a, b = map(int, input().split())

a -= 1
b -= 1

row = abs(a//4 - b//4)
col = abs(a%4 - b%4)

print(row + col)