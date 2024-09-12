T = int(input())

for i in range(T):
    N = int(input())
    
    if int(str(N**2)[-len(str(N)):]) == N:
        print('YES')
    else:
        print('NO')