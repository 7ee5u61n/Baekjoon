q = int(input())
for _ in range(q):
    s = str(input())
    result = 0
    for i in range(len(s)-2):
        if s[i:i+3] == 'WOW':
            result += 1
    print(result)