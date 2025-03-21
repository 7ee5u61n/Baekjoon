import sys
input = sys.stdin.readline

n = int(input())
for _ in range(n):
    m = int(input())
    end = False
    for i in range(64):
        if not end:
            for j in range(i, 64):
                if 2**i + 2**j == m:
                    end = True
                    print(i, j)
                    break
        else:
            break