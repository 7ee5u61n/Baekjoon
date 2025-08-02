m = int(input())

result = 0
for i in range(m):
    if i < 30:
        result += 0.5
    else:
        result += 1.5

print(f'{result:.1f}')