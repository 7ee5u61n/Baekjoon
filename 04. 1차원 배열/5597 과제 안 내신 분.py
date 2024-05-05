n = list(range(1, 31)) # 출석번호 1~30

submitList = [] # 제출한 학생 리스트

for i in range(28):
    submitId = int(input()) # 제출한 학생 번호
    submitList.append(submitId)

unsubmitList = set(n) - set(submitList) # 안낸 학생 번호
unsubmitList = sorted(list(unsubmitList))

for i in range(2):
    print(unsubmitList[i])