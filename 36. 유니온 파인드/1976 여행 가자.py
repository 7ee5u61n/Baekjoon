def find_parent(x):
    if parent[x] != x:
        parent[x] = find_parent(parent[x])
    return parent[x]

def union_parent(a, b):
    a = find_parent(a)
    b = find_parent(b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b

n = int(input())
m = int(input())

parent = [i for i in range(n)]
for i in range(n):
    route = list(map(int, input().split()))
    for j in range(n):
        if route[j]:
            union_parent(i, j)
parent = [-1] + parent

plan = list(map(int, input().split()))
start = parent[plan[0]]
check = True
for i in range(1, m):
    if parent[plan[i]] != start:
        check = False
        break

if check:
    print('YES')
else:
    print('NO')