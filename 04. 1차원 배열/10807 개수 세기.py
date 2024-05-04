import sys

N = int(input()) # 1번째 줄: 정수의 개수

intInput = [] 

while True:
    intInput = list(map(int, sys.stdin.readline().split()))
    # 2번째 줄: 정수를 공백으로 구분하여 입력
    if len(intInput) == N:
        break

v = int(input()) # 3번째 줄: 찾으려는 정수

count = intInput.count(v) # 몇 개?
print(count)