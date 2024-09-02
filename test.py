T = int(input())
score = [0]*5
base = list(map(int, input().split()))

for i in range(T):
    score[i] = base[i]

studentID = 0
if score[0] > score[2]:
    studentID += (score[0] - score[2]) * 508
else:
    studentID += (score[2] - score[0]) * 108

if score[1] > score[3]:
    studentID += (score[1] - score[3]) * 212
else:
    studentID += (score[3] - score[1]) * 305

if score[4]:
    studentID += score[4] * 707

studentID *= 4763

print(studentID)