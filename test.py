N, T = map(int, input().split())

result = []
for _ in range(N):
    S, I, C = map(int, input().split())
    
    bus_time = [S+I*i for i in range(C)]
    if bus_time[-1] < T:
        continue

    start = 0
    end = C - 1
    target = 0
    while start <= end:
        mid = (start + end) // 2
        if bus_time[mid] >= T:
            target = mid
            end = mid - 1
        else:
            start = mid + 1

    result.append(bus_time[target] - T)

if result:
    print(min(result))
else:
    print(-1)