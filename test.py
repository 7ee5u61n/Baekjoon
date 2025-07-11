p = list(float(input()) for _ in range(10))
p.sort(reverse=True)
result = 1
for i in range(1, 10):
    result *= p[i-1]/i

result *= int(1e9)
print(round(result, 6))