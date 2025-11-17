n, m = map(int, input().split())

board = [int(input()) for _ in range(n)]

result = 0
locate = 0
for j in range(m):
    dice = int(input())
    locate += dice
    locate += board[locate%n]

    if locate >= n-1 and result == 0:
        result = j + 1

print(result)