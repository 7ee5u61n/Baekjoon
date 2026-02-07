a = 'SciComLove'
s = str(input())

result = 0
for i in range(len(a)):
    if a[i] != s[i]:
        result += 1

print(result)