N = int(input())

highScore = 0
for _ in range(N):
    score = list(map(int, input().split()))
    highRun = score[0:2]
    highTrick = score[2:7]

    highRun.sort(reverse=True)
    highTrick.sort(reverse=True)

    score = highRun[0] + highTrick[0] + highTrick[1]
    if highScore < score:
        highScore = score

print(highScore)