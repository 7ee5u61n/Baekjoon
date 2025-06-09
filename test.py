        # 허들
calc = [[9.23076, 26.7, 1.835, 0], 
        # 높이뛰기
        [1.84523, 75, 1.348, 1],
        # 포환
        [56.0211, 1.5, 1.05, 1], 
        # 200 달리기
        [4.99087, 42.5, 1.81, 0],
        # 멀리뛰기
        [0.188807, 210, 1.41, 1], 
        # 창던지기
        [15.9803, 3.8, 1.04, 1],
        # 800 달리기기
        [0.11193, 254, 1.88, 0]]


n = int(input())
for _ in range(n):
    case = list(map(int, input().split()))
    result = 0
    for i in range(7):
        a = calc[i][0]
        b = calc[i][1]
        c = calc[i][2]
        kind = calc[i][3]
        p = case[i]

        # 트랙
        if kind == 0:
            result += int(a*(b-p)**c)
        # 필드
        else:
            result += int(a*(p-b)**c)

    print(result)