T = int(input())

for _ in range(T):
    n = int(input())
    total = 0
    gpa = 0
    for _ in range(n):
        c, g = map(float, input().split())
        total += c
        gpa += c * g

    print(int(total), round(gpa / total, 1))