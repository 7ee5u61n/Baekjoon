N = int(input())

paint = []
for _ in range(N):
    temp = []
    for _ in range(5):
        temp.append(input().rstrip())
    paint.append(temp)

arr = []
least_diff = 36
for i in range(N-1):
    for j in range(i+1, N):
        diff = 0
        for k in range(5):
            for l in range(7):
                if paint[i][k][l] != paint[j][k][l]:
                    diff += 1
        if least_diff > diff:
            least_diff = diff
            arr = [i+1, j+1]

print(*arr)