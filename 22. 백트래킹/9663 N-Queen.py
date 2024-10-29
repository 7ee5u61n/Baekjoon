def dfs(queen):
    global result

    if queen == n:
        result += 1
        return
    
    for i in range(n):
        if column[i] == dia1[queen+i] == dia2[queen-i] == 0:
            column[i] = dia1[queen+i] = dia2[queen-i] = 1
            dfs(queen+1)
            column[i] = dia1[queen+i] = dia2[queen-i] = 0
            
n = int(input())

column = [0]*n
dia1 = [0]*(2*n)
dia2 = [0]*(2*n)

result = 0
dfs(0)
print(result)