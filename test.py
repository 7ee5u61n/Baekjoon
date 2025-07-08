n = int(input())
s = str(input())

alphabet = [0]*26
for i in range(n):
    if n % 2:
        if i == n//2:
            continue
    index = ord(s[i])-97
    alphabet[index] += 1

palidrome = True
for i in alphabet:
    if i % 2:
        palidrome = False
        break

if palidrome:
    print('Yes')
else:
    print('No')