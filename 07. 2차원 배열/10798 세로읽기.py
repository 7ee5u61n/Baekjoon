matrix = []

for _ in range(5): 
    value = list(input().rstrip())
    matrix.append(value)

for i in range(15):
    for j in range(15):
        try:
            print(matrix[j][i], end='')
        except:
            pass
