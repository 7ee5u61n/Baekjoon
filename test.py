n = int(input())

for _ in range(n):
    s = str(input())
    if s[:10] == 'Simon says':
        print(s[10:])