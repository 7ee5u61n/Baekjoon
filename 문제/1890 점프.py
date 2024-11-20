n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
dp = [[0]*n for _ in range(n)]

# 첫 칸에서 갈 수 있는 곳
dp[board[0][0]][0] = 1
dp[0][board[0][0]] = 1

for i in range(n):
    for j in range(n):
        # 위쪽 칸 확인
        for k in range(1, 10):
            if 0 <= i-k < n and board[i-k][j] == k:
                dp[i][j] += dp[i-k][j]
        # 왼쪽 칸 확인
        for k in range(1, 10):
            if 0 <= j-k < n and board[i][j-k] == k:
                dp[i][j] += dp[i][j-k]

print(dp[n-1][n-1])
