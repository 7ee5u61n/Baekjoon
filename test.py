l, r, a = map(int, input().split())

# 왼발, 오른발 같을 때 까지
while l != r:
    if l > r:
        # 양발 있으면
        if a:
            a -= 1
            r += 1
        # 없으면
        else:
            l -= 1
    elif l < r:
        if a:
            a -= 1
            l += 1
        else:
            r -= 1
if a % 2 == 1:
    a -= 1

print(l+r+a)