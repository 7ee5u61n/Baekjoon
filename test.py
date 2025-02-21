import sys

triNum = []
for i in range(1, 1001):
    triNum.append(i*(i+1)//2)

T = int(sys.stdin.readline())
for _ in range(T):
    K = int(sys.stdin.readline())

    possible = False
    for i in range(K):
        for j in range(i, K):
            for k in range(j, K):
                if triNum[i]+triNum[j]+triNum[k] == K:
                    possible = True
                    break
            if possible:
                break
        if possible:
            break
    
    if possible:
        print(1)
    else:
        print(0)