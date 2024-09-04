N = int(input())
mascot = str(input())
K = int(input())

if mascot == 'annyong':
    if K % 2 == 0:
        print(K-1)
    else:
        print(K)

else:
    if K % 2 == 0:
        print(K)
    elif K-1 == 0:
        print(K+1)
    else:
        print(K-1)