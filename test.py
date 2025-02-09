n = int(input())
file = [input() for _ in range(n)]

result = ''
for i in range(len(file[0])):
    temp = file[0][i]
    for j in range(1, n):
        if file[j][i] != temp:
            temp = '?'
            break
    result += temp

print(result)