ignore = {'i', 'pa', 'te', 'ni', 'niti', 'a', 'ali', 'nego', 'no', 'ili'}

s = list(map(str, input().split()))

result = ''
for i in range(len(s)):
    if i > 0 and s[i] in ignore:
        continue
    result += s[i][0].upper()

print(result)