n = int(input())
s = str(input())

for i in range(n):
    if s[i].isupper():
        print(s[i].lower(), end='')
    else:
        print(s[i].upper(), end='')

