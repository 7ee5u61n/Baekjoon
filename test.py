n = int(input())
s = str(input())

color = {'R':0, 'B':0}
color[s[0]] = 1

for i in range(1, n):
    if s[i-1] != s[i]:
        color[s[i]] += 1

result = min(color['R'], color['B']) + 1

print(result)