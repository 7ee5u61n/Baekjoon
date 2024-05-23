while True:
    A, B = map(int, input().split())
    if A > B:
        divide = A / B # A 가 B의 배수인지 확인
        if divide == int(divide):
            print('multiple')
        else:
            print('neither')
    if A < B:
        divide = B / A # A가 B의 약수인지 확인
        if divide == int(divide):
            print('factor')
        else:
            print('neither')
    if A == 0 and B == 0:
        break