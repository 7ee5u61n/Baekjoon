def dfs(count, result):
    global max_value, min_value

    if count == n:
        max_value = max(max_value, result)
        min_value = min(min_value, result)
        return
    
    for i in range(4):
        if oper[i]:
            oper[i] -= 1
            # 덧셈
            if i == 0:
                dfs(count+1, result+a[count])
            # 뺄셈
            elif i == 1:
                dfs(count+1, result-a[count])
            # 곱셈
            elif i == 2:
                dfs(count+1, result*a[count])
            # 나눗셈
            elif i == 3:
                dfs(count+1, int(result/a[count]))
            oper[i] += 1

n = int(input())
a = list(map(int, input().split()))

oper = list(map(int, input().split()))

max_value = int(-1e9)
min_value = int(1e9)

dfs(1, a[0])

print(max_value)
print(min_value)