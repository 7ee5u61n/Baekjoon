N = int(input()) # 판매하는 무기의 수
X, S = map(int, input().split()) # 가진 돈 X, 후안의 공격력 S

weapon = []
for i in range(N): #
    c, p = map(int, input().split())
    if c <= X and p > S:
        weapon.append(True) # 가격이 가진 돈보다 작고 무기 공격력이 후안의 공격력보다 크면 구입

if bool(weapon) == True:
    print('YES')
else:
    print('NO')