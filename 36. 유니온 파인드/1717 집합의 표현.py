import sys
sys.setrecursionlimit(100000)

# find
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

# union
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b

# 집합의 개수, 연산의 개수
n, m = map(int, sys.stdin.readline().split())

parent = [0]*(n+1)

for i in range(n+1):
    parent[i] = i

for _ in range(m):
    calc, a, b = map(int, sys.stdin.readline().split())

    # 0이면 union
    if calc == 0:
        union_parent(parent, a, b)
    # 1이면 find
    else:
        # 포함되어 있으면 YES 출력
        if find_parent(parent, a) == find_parent(parent, b):
            print('YES')
        else:
            print('NO')