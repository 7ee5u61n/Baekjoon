N, K = map(int, input().split())

count = 0
for i in range(N+1):
    for j in range(60):
        for k in range(60):
            time = str(i).zfill(2) + str(j).zfill(2) + str(k).zfill(2)
            if str(K) in time:
                count += 1

print(count)