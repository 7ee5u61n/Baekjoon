n = int(input())
a = list(map(int,input().split()))

b = list(a)
b.sort()

l = 1
op = 0
arr = []
while a != b:
    if a[l-1] != l:
        r = a.index(l)+1
        a[l-1:a.index(l)+1] = a[l-1:a.index(l)+1][::-1]
        arr.append([l,r])
        op += 1
    l += 1

print(op)
for i in arr:
    print(*i)