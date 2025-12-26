s, d, i, l, n = map(int, input().split())
avg = (s + d + i + l) / 4

result = 0
while avg < n:
    avg += 0.25
    result += 1

print(result)