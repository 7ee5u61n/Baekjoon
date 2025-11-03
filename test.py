T = int(input())
for _ in range(T):
    arr = list(map(int, input().split()))
    max_val = max(arr)
    min_val = min(arr)

    arr.remove(max_val)
    arr.remove(min_val)

    max_val = max(arr)
    min_val = min(arr)

    if max_val - min_val >= 4:
        print('KIN')
    else:
        print(sum(arr))