import sys

N = int(input()) # 시험 본 과목의 개수

while True:
    jumsu = list(map(int, sys.stdin.readline().split()))
    if len(jumsu) == N: # 과목의 수와 점수의 수가 일치하지 않으면 다시
        break
    else:
        print('점수 다시')

M = max(jumsu) # 점수 최댓값

fixJumsu = [] # 고친 점수 리스트

for i in range(len(jumsu)):
    fixJumsu.append(jumsu[i]/M*100) # 세준이 점수 고침

fixJumsuAvg = sum(fixJumsu)/N # 고친 점수 평균

print(fixJumsuAvg)