T = int(input())
for _ in range(T):
    n = int(input())

    base = list(input())
    goal = list(input())

    wrongB = 0
    wrongW = 0

    for i in range(n):
        if base[i] != goal[i]:
            if base[i] == 'B':
                wrongB += 1
            else:
                wrongW += 1

    if wrongB >= wrongW:
        result = wrongB
    else:
        result = wrongW

    print(result)