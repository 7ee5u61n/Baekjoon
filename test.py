n = int(input())
# 국가별 메달 수
medal = [0]*101

info = []
for _ in range(n):
    info.append(list(map(int, input().split())))

info.sort(key= lambda x : x[2], reverse=True)

# 금, 은, 동
winner = 0
for country, student, score in info:
    if winner >= 3:
        break
    if medal[country] < 2:
        medal[country] += 1
        winner += 1
        print(country, student)