n = int(input())
student = []
for _ in range(n):
    student.append(''.join(reversed(str(input()))))

word = len(student[0])
for i in range(1, word+1):
    number = []
    for j in range(n):
        number.append((student[j])[:i])
    if len(number) == len(list(set(number))):
        break

print(i)