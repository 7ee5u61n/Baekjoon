n, m = map(int, input().split())

lecture = {}

for i in range(n):
    k = int(input())
    student = list(map(int, input().split()))

    for j in range(k):
        if student[j] in lecture:
            lecture[student[j]] += 1
        else:
            lecture[student[j]] = 1

result = 0
for k, v in lecture.items():
    if v >= m:
        result += 1

print(result)