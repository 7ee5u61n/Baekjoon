# 전공평점 = (학점 * 과목평점) / 학점의 총합
totalCredit = 0 # 학점 총점
gcd = 0 # 전공과목별 (학점*과목평점)의 합

for i in range(20):
    subject, credit, grade = input().split()
    gradePoint = 0
    if grade != 'P':
        totalCredit += float(credit)
    if grade == 'A+':
        gradePoint = 4.5
    elif grade == 'A0':
        gradePoint = 4.0
    elif grade == 'B+':
        gradePoint = 3.5
    elif grade == 'B0':
        gradePoint = 3.0
    elif grade == 'C+':
        gradePoint = 2.5
    elif grade == 'C0':
        gradePoint = 2.0
    elif grade == 'D+':
        gradePoint = 1.5
    elif grade == 'D0':
        gradePoint = 1.0
    elif grade == 'F':
        gradePoint = 0
    gcd += float(credit) * gradePoint

# print(gcd)
# print(totalCredit)
try:
    majorCredit = gcd / totalCredit # 전공평점
    print(majorCredit)
except ZeroDivisionError: # 전부 F맞아서 평점이 0이면 전공평점 0
    print(0)