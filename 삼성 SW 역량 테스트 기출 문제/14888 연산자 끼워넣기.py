def calc(count, result, add, sub, mul, div):
    global mx
    global mn
    
    if count == n:
        mx = max(mx, result)
        mn = min(mn, result)
        return
    # 덧셈
    if add > 0:
        calc(count+1, result+a[count], add-1, sub, mul, div)
    # 뺄셈
    if sub > 0:
        calc(count+1, result-a[count], add, sub-1, mul, div)
    # 곱셈
    if mul > 0:
        calc(count+1, result*a[count], add, sub, mul-1, div)
    # 나눗셈
    if div > 0:
        calc(count+1, int(result/a[count]), add, sub, mul, div-1)


n = int(input())
a = list(map(int, input().split()))

# 덧셈, 뺄셈, 곱셈, 나눗셈
oper = list(map(int, input().split()))

mx = -(10**9)-1
mn = 10**9+1

calc(1, a[0], oper[0], oper[1], oper[2], oper[3])

print(mx)
print(mn)