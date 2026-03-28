n = int(input())
s = str(input())

h, i, a, r, c = 0, 0, 0, 0, 0

for char in s:
    if char == 'H':
        h += 1
    elif char == 'I':
        i += 1
    elif char == 'A':
        a += 1
    elif char == 'R':
        r += 1
    elif char == 'C':
        c += 1    

print(min(h, i, a, r, c))