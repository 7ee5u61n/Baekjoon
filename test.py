A, B = map(int, input().split())
C, D = map(int, input().split())

number = [A, B, D, C]
max = number[0] / number[3] + number[1] / number[2]
count = 0
for i in range(4):
    value = number[0] / number[3] + number[1] / number[2]
    if value > max:
        max = value
        count = i

    number.insert(0, number.pop())
    
print(count)