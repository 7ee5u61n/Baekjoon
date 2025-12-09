n = int(input())
n //= 3

result = 0
for i in range(n-1):
    result += i

print(result)