n, m = map(int, input().split())
bottom = input()

able = True
for i in range(n-1):
    top = input()
    able = False
    for j in range(1, m+1):
        if top[m-j:] == bottom[:j] or top[:j] == bottom[m-j:]:
            bottom = top
            able = True
            break

    if not able:
        break
    
if able:
    print(1)
else:
    print(0)