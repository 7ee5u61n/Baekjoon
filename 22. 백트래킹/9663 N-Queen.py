import sys

def check(x):
    for i in range(x):
        # 같은 열이나 대각선에 있을 때
        if row[x] == row[i] or abs(row[x]-row[i]) == abs(x-i):
            return False
    return True

def dfs(count):
    global result

    if count == n:
        result += 1
        return
    else:
        for i in range(n):
            row[count] = i
            if check(count):
                dfs(count+1)

n = int(sys.stdin.readline())

row=[0]*n
result = 0

dfs(0)
print(result)