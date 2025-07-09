n, m = map(int, input().split())
teacher = []
for _ in range(n):
    teacher.append(input())

escape = False
for i in range(m):
    count = 0
    for j in range(n):
        if teacher[j][i] == 'O':
            break
        else:
            count += 1

    if count == n:
        escape = i+1
        break

if escape:
    print(escape)
else:
    print('ESCAPE FAILED')