n = int(input())
arr = [list(input()) for _ in range(n)]

# 심장 위치
row = 0 
col = 0
for i in range(n):
    if row != 0 and col != 0:
        break
    for j in range(n):
        if arr[i][j] == '*':
            row = i+1
            col = j
            break

leftArm = 0
rightArm = 0
waist = 0
leftLeg = 0
rightLeg = 0

for i in range(1, n):
    if (0 <= row < n) and (0 <= col-i < n) and arr[row][col-i] == '*':
        leftArm += 1
    
    if (0 <= row < n) and (0 <= col+i < n) and arr[row][col+i] == '*':
        rightArm += 1
    
    if (0 <= row+i < n) and (0 <= col < n) and arr[row+i][col] == '*':
        waist += 1
    elif (0 <= row+i < n) and (0 <= col < n) and arr[row+i][col] == '_':
        if arr[row+i][col-1] == '*':
            leftLeg += 1
        if arr [row+i][col+1] == '*':
            rightLeg += 1  
        
print(row+1, col+1)
print(leftArm, rightArm, waist, leftLeg, rightLeg)