h, w = map(int, input().split())
weather = [list(input()) for _ in range(h)]

cloud = [[-1]*w for _ in range(h)]

for i in range(h):
    for j in range(w):
        if weather[i][j] == 'c':
            for k in range(w-j):
                cloud[i][j+k] = k

for i in range(h):
    for j in range(w):
        print(cloud[i][j], end=' ')
    print('')