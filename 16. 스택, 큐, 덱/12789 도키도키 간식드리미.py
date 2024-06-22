import sys

N = int(input())

inLine = list(map(int, input().split())) # 현재 줄 서있는 곳

wait = [] # 한 명씩만 설 수 있는 공간에 대기하고 있는 사람
count = 1 # 현재 간식 받는 번호

for i in inLine:
    wait.append(i)
    while wait and wait[-1] == count:
        wait.pop()
        count += 1

    if len(wait) > 1 and wait[-1] > wait[-2]:
        print('Sad')
        sys.exit()
if wait:
    print('Sad')
else:
    print('Nice')