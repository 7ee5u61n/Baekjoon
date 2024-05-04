import sys

#수열을 이루는 정수 N, 비교할 수 X
N, X = map(int, input().split()) 
# 정수 N개로 이루어진 수열 A
A = []
# 수열 A에서 X보다 작은 수를 저장하는 리스트
result = []

while True:
    # 2번째 줄: 정수를 공백으로 구분하여 입력
    A = list(map(int, sys.stdin.readline().split()))
    
    # 입력한 정수가 N과 일치해야 진행
    if len(A) == N:
        break

# 테스트용
# print(N, X, A[1])

for i in range(len(A)):
    if A[i] < X:
        result.append(A[i])

# 결과 한 줄로 출력
print(*result)