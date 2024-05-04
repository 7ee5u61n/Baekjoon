import sys

nList = [] # 자연수가 들어갈 리스트

for i in range(9):
    N = int(sys.stdin.readline().rstrip()) # 한 줄 씩 자연수 입력
    nList.append(N) # 입력한 자연수 리스트에 저장

print(max(nList)) # 최댓값 출력
print(int(nList.index(max(nList)))+1) # 최댓값 몇 번째