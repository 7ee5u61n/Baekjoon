n, m = map(int, input().split())
result = 1
for _ in range(n):
    a = int(input())
    if a != 0:
        result *= a 
        
print(result%m)