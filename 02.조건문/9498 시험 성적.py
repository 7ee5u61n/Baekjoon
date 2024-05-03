score = int(input())

while score < 0 or score > 100:
    print('올바른 점수가 아닙니다.')
    score = int(input())

if score >= 90:
    print('A')
elif score >= 80:
    print('B')
elif score >= 70:
    print('C')
elif score >= 60:
    print('D')
else:
    print('F')