T = int(input())
for test_case in range(1, T+1):
    k = int(input())
    n = int(input())
    floor = [i for i in range(1, n+1)]
    
    for i in range(k):
        for j in range(1, n):
            floor[j] += floor[j-1]

    print(floor[-1])