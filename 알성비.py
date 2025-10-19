s = str(input())

result = 0
for i in range(len(s)-3):
    if s[i:i+4] == 'DKSH':
        result += 1

print(result)