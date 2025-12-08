a, b = map(int, input().split())

result = 1
for i in range(a, b+1):
    temp = i*(i+1)//2
    result *= temp

print(result%14579)