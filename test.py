# 약수의 개수
def diviosr(x):
    count = 0
    # 1을 제외한 약수의 개수
    for i in range(2, x+1):
        if x % i == 0:
            count += 1
    return count

# 메모이제이션
d = [0] * 101
def dynamic(x):
    if x == 2 or x== 3:
        return 1
    if d[x] != 0:
        return d[x]
    d[x] = diviosr(x)
    return d[x]

t = int(input())

for _ in range(t):
    n = int(input())
    # True일 때 탈출 가능
    room = [True] * (n+1)
    room[0] = 0
    for i in range(1, n+1):
        # 약수의 개수가 홀수일 때
        if dynamic(i) % 2 == 1:
            room[i] = False
        # 짝수일 때
        else:
            room[i] = True

    # 탈출할 수 있는 
    print(room.count(True))