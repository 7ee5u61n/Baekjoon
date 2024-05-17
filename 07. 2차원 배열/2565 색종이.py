N = int(input()) # 색종이의 수
paper = []

for _ in range(N):
    x, y = map(int, input().split()) # 색종이를 붙인 좌표(좌하단 꼭지점)
    for i in range(y, y+10):
        for j in range(x, x+10):
            if [j,i] not in paper:
                paper.append([j, i])
            
print(len(paper))