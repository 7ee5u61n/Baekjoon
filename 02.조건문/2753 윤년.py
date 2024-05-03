year = int(input())

while year > 4000 or year < 1:
    print('혹시 오타 아니야? 1~4000 사이 년도만 입력해줘! 다시 입력해 (1~4000)')
    year = int(input())
if year % 4 == 0 and year % 100 != 0:
    print(1)
elif year % 400 == 0:
    print(1)
else:
    print(0)