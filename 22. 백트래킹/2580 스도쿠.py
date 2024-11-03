def checkRow(x, a):
    for i in range(n):
        # 해당 행에 이미 숫자가 있을 경우
        if sudoku[x][i] == a:
            return False
    return True

def checkColumn(y, a):
    for i in range(n):
        if sudoku[i][y] == a:
            return False
    return True

def checkRoom(x, y, a):
    for i in range(x//3*3, x//3*3+3):
        for j in range(y//3*3, y//3*3+3):
            if sudoku[i][j] == a:
                return False
            
    return True

def solve(count):
    # 빈칸 다 채우면 종료
    if count == len(blank):
        for i in sudoku:
            print(*i)
        exit()

    x, y = blank[count]
    for i in range(1, n+1):
        if checkRow(x, i) and checkColumn(y, i) and checkRoom(x, y, i):
            sudoku[x][y] = i
            solve(count+1)
            sudoku[x][y] = 0

n = 9
sudoku = [list(map(int, input().split())) for _ in range(n)]
# 빈칸 좌표
blank = []
for i in range(n):
    for j in range(n):
        if sudoku[i][j] == 0:
            blank.append((i, j))

solve(0)