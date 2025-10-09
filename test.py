a, b, c = map(int, input().split())

result1 = a*b/c
result2 = a/b*c

print(int(max(result1, result2)))