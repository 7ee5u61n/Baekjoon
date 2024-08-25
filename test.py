def workTime(X):
    # 1은 출근, 2는 퇴근, 3은 근무시간
    h1 = X[0]
    m1 = X[1]
    s1 = X[2]
    h2 = X[3]
    m2 = X[4]
    s2 = X[5]

    h3 = 0
    m3 = 0
    s3 = 0
    
    if s2-s1<0:
        m2-=1
        s3 = s2-s1+60
    else:
        s3 = s2-s1
    if m2-m1<0:
        h2-=1
        m3 = m2-m1+60
    else:
        m3 = m2-m1
    h3 = h2-h1

    return h3, m3, s3

for _ in range(3):
    X = list(map(int, input().split()))
    print(*workTime(X))