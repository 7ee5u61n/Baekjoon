N = [int(input()) for i in range(10)] # 10개의 수를 입력
v = len(N) 
remains = []

for i in range(v):
    remains.append(N[i] % 42) # 42로 나눈 나머지 저장

result = []
for i in remains: # 나머지 리스트에서 중복 제거
    if i not in result:
        result.append(i)

print(len(result))