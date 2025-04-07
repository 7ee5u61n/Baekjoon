n , m = map(int, input().split())

entry = list(0 for _ in range(n+1))
blue = []
white = []

while True:
    classNumber, studentName = input().split()
    if classNumber == '0' and studentName == '0':
        break

    classNumber = int(classNumber)

    if entry[classNumber] < m:
        if classNumber % 2 == 1:
            blue.append((classNumber, studentName))
        else:
            white.append((classNumber, studentName))

        entry[classNumber] += 1

blue.sort(key= lambda x: (x[0], len(x[1]), x[1]))
white.sort(key= lambda x: (x[0], len(x[1]), x[1]))

result = blue + white

for i in result:
    print(*i)