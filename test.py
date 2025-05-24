n = int(input())
tap = [0]*367
space = [0]*367
start = 366
end = 0
longest = 0
for _ in range(n):
    c, s, e = input().split()
    s = int(s)
    e = int(e)
    start = min(s, start)
    end = max(e, end)
    longest = max(e-s+1, longest)

    if c == 'T':
        for i in range(s, e+1):
            tap[i] += 1
    else:
        for i in range(s, e+1):
            space[i] += 1

info = [0]*6
for i in range(start, end+1):
    # 1. 투수객이 1명 이상
    if tap[i] > 0 or space[i] > 0:
        info[1] += 1
    # 2. 가장 많은 투숙객이 있었던 날에 투숙한 사람 수 
    if tap[i] + space[i] > info[2]:
        info[2] = tap[i] + space[i]
    # 3. 싸움이 없는 날의 수 
    if (tap[i] or space[i]) and tap[i] == space[i]:
        info[3] += 1
        # 4. 싸움이 없는 날 중 가장 많은 투숙객이 있었던 날에 투숙한 사람의 수. 싸움이 없는 날이 없으면 0을 출력
        if tap[i] + space[i] > info[4]:
            info[4] = tap[i] + space[i]
# 5. 가장 오랜 기간 투숙한 사람이 투숙한 날의 수
info[5] = longest

for i in range(1, 6):
    print(info[i])