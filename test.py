a = str(input())
b = str(input())

stroke = [3, 2, 1, 2, 3, 3, 2, 3, 3, 2, 2, 1, 2, 2, 1, 2, 2, 2, 1, 2, 1, 1, 1, 2, 2, 1]

number = ''
for i in range(len(a)):
    number += str(stroke[ord(a[i])-65])
    number += str(stroke[ord(b[i])-65])


for i in range(len(a)*2-2):
    now = ''
    for j in range(len(number)-1):
        if int(number[j]) + int(number[j+1]) >= 10:
            now += str(int(number[j]) + int(number[j+1]) - 10)
        else:
            now += str(int(number[j]) + int(number[j+1]))
    number = now

print(number)