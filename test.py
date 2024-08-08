def getChicken(X):
    if N >= X:
        get = X
    else:
        get = N
    return get

N = int(input())
A, B, C = map(int, input().split())

print(getChicken(A)+getChicken(B)+getChicken(C))