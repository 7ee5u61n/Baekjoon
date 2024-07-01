N = int(input())

result = 1
for i in range(N-1):
    result *= N
    N -= 1

print(result)