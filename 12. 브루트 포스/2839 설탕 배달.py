# 3=1, 5=1, 8=2, 9=3, 10=2, 11=3, 14=3, 15=3, 16=4, 18=4, 21, 23, 24, 26, 27, 29, 30
N = int(input())
pack = []

if N % 5 == 0: # 5킬로 봉지만 이용해서 담을 경우
    print(N // 5)
else:
    pack = 0
    while N > 0: # 5킬로, 3킬로 섞어 담는 경우
        N -= 3
        pack += 1
        if N % 5 == 0:
            pack += N // 5
            print(pack)
            break
        elif N == 0: # 3킬로만 담는 경우
            print(pack)
            break
        elif N <= 2: # N킬로 만들 수 없는 경우
            print(-1) 
            break