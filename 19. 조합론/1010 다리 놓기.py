T = int(input())

for _ in range(T):
    N, M = map(int, input().split())
    result = 1
    
    for _ in range(N):
        result *= M
        M -= 1
    for _ in range(N):
        result //= N
        N -= 1
    
    print(result)