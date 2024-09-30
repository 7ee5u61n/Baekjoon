# 플레이어 수
N = int(input())
# 투표한 번호
X = list(map(int, input().split()))
# 받은 투표 수
player = dict()
for i in range(N):
    player[i+1] = 0

for i in range(N):
    vote = X[i]
    if vote != 0:
        player[vote] += 1

# 가장 많이 표를 받은 사람
imposter = [k for k,v in player.items() if max(player.values()) == v]

if len(imposter) == 1:
    print(*imposter)
else:
    print('skipped')