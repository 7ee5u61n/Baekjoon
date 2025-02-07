x, y = map(int, input().split())
row = [0, x]
column = [0, y]

n = int(input())
for _ in range(n):
    a, b = map(int, input().split())
    if a == 0:
        column.append(b)
    else:
        row.append(b)

row.sort()
column.sort()

result = 0
for i in range(1, len(row)):
    for j in range(1, len(column)):
        width = row[i] - row[i-1]
        height = column[j] - column[j-1]
        result = max(result, width*height)

print(result)