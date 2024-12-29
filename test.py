n = int(input())
text = list(str(input()) for _ in range(n))

number = []
for i in range(n):
    num = ''
    for j in range(len(text[i])):
        if text[i][j].isnumeric():
            num += text[i][j]
        else:
            if num:
                number.append(int(num))
            num = ''
    if num:
        number.append(int(num))

number.sort()
for i in number:
    print(i)