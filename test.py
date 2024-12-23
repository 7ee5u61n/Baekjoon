n, m = map(int, input().split())
a = list(map(int, input().split()))
a.sort()

for _ in range(m):
    order = list(map(int, input().split()))
    # k보다 크거나 같은 원소
    if order[0] == 1:
        count = 0
        for i in range(n-1, -1, -1):
            if a[i] >= order[1]:
                count += 1
            else:
                break
        print(count)
    
    # k보다 큰 원소
    elif order[0] == 2:
        count = 0
        for i in range(n-1, -1, -1):
            if a[i] > order[1]:
                count += 1
            else:
                break
        print(count)

    # i보다 크거나 같고 j보다 작거나 같은 원소
    else:
        count = 0
        for i in range(n):
            if order[1] <= a[i] <= order[2]:
                count += 1
            elif a[i] > order[2]:
                break
        print(count)