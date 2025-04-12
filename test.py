doc = list(input())
search = list(input())
n = len(search)

result = 0
for i in range(len(doc)):
    if doc[i:i+n] == search:
        result += 1
        for j in range(i, i+n):
            doc[j] = ''

print(result)