A, B = list(map(str, input().split())) # 0이 포함되어 있지 않고 같지 않은 두개의 세자리 수

if int(A[::-1]) > int(B[::-1]):
    print(A[::-1])
else:
    print(B[::-1])