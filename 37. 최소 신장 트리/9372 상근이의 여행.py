def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b

t = int(input())

for _ in range(t):
    # 국가의 수, 비행기 종류
    n, m = map(int, input().split())

    # 부모 테이블 초기화
    parent = [0]*(n+1)
    for i in range(1, n+1):
        parent[i] = i

    # 비행기 탑승 횟수
    result = 0
    for i in range(m):
        a, b = map(int, input().split())
        # 사이클이 존재하지 않으면 비행기 탑승
        if find_parent(parent, a) != find_parent(parent, b):
            union_parent(parent, a, b)
            result += 1

    print(result)