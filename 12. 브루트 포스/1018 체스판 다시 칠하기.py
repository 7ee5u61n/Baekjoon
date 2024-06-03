N, M=map(int,input().split())

line = []
result = []
for i in range(N):
    line.append(input())
    
for row in range(N-7):
    for col in range(M-7):
        wStart=0 # 흰색으로 시작
        bStart=0 # 검은색으로 시작
        
        for i in range(row, row+8):
            for j in range(col, col+8):
                if (i+j)%2 == 0:
                    if line[i][j]!='W':
                        wStart += 1
                    else:
                        bStart += 1
                else:
                    if line[i][j]!='W':
                        bStart+=1
                    else:
                        wStart+=1
                        
        result.append(wStart) 
        result.append(bStart) 
print(min(result))