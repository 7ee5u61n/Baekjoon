s, n, m = map(int, input().split())

arr = []
for i in range(n+m):
    o = int(input())
    if o == 1:
        if len(arr)+1 > s:
            s *= 2
        arr.append(o)
    else:
        arr.pop()

print(s)