n = int(input())
a = list(map(str, input().split()))
student = {}
for i in range(n):
    student[a[i]] = 0

for _ in range(n):
    like = list(map(str, input().split()))
    for i in range(len(like)):
        student[like[i]] += 1

result = []
for key, value in student.items():
    result.append([key, value])

result.sort(key=lambda x: (-x[1], x[0]))

for i, j in result:
    print(i, j)