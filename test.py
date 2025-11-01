n = int(input())

result = 0
for _ in range(n):
    s = str(input())
    for i in range(len(s)-1):
        if s[i:i+2] == '01' or s[i:i+2] == 'OI':
            result += 1
            break

print(result)