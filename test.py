n = int(input())
seat = [['.' for _ in range(20)] for _ in range(10)]

for _ in range(n):
    s = str(input())
    row = ord(s[0]) - ord('A')
    col = int(s[1:]) - 1
    seat[row][col] = 'o'

for i in range(10):
    for j in range(20):
        print(seat[i][j], end='')
    print()