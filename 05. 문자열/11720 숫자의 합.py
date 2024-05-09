while True:
    N = int(input()) # 숫자의 개수
    if (1 <= N <= 100):
        break
    else:
        print('1~100 사이의 정수를 입력하시오')
while True:
    S = list(map(int, input())) # 공백없이 숫자 N개
    if len(S) == N:
        break
    else:
        print('N 개의 숫자를 입력하시오')
print(sum(S)) # 숫자들의 합