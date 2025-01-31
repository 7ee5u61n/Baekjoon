s = str(input())
count = 0
number = s[0]
for i in range(1, len(s)):
    if int(s[i]) - int(s[i-1]) == 1:
        number += s[i]
    else:
        if len(number) == 3:
            count += 1
        number = s[i]

if len(number) == 3:
    count += 1

print(count)