N, M = map(int, input().split()) # 바구니 N개, 공을 M번 넣기
N = [0]*N # 빈 바구니 0번으로 초기화

for _ in range(M):
    i, j, k = map(int, input().split()) # i번 부터 j번 바구니까지 k번 공을 넣는다. 
    for n in range(i-1, j): # i번 부터 j번 바구니 까지
        N[n] = k # k번 공을 넣음

result = " ".join(map(str, N)) # 공백으로 구분하여 한 줄에 출력
print(result)