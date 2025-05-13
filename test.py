j = int(input())
a = int(input())

jersey = ['X']
for i in range(j):
    jersey.append(str(input()))

result = 0
for i in range(a):
    size, number = input().split()
    number = int(number)

    if jersey[number] != 'X':
        if size == 'S':
            jersey[number] = 'X'
            result += 1
        elif size == 'M':
            if jersey[number] != 'S':
                jersey[number] = 'X'
                result += 1
        else:
            if jersey[number] == 'L':
                jersey[number] = 'X'
                result += 1

print(result)