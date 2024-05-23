N, K = map(int, input().split())
divisor = [] # 약수를 저장하는 리스트

for i in range(N):
    if N % (i+1) == 0:
        divisor.append(int(N/(i+1))) 
divisor = sorted(divisor)

if len(divisor) < K:
    print(0)
else:
    print(divisor[K-1])