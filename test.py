n = int(input())
arr = list(map(int, input().split()))

odd = 0
even = 0
for i in range(n):
    if arr[i] % 2:
        odd += 1
    else:
        even += 1

if n % 2:
    if odd - even == 1:
        print(1)
    else:
        print(0)
else:
    if odd == even:
        print(1)
    else:
        print(0)