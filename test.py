r, c, n = map(int, input().split())

result = 1
if r%n == 0:
    result *= r//n
else:
    result *= r//n+1

if c%n == 0:
    result *= c//n
else:
    result *= c//n+1

print(result)