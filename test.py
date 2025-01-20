n = str(input())
if len(n) % 3 == 1:
    n = '00' + n
elif len(n) % 3 == 2:
    n = '0' + n

number = ''
for i in range(0, len(n), 3):
    number += str(int(n[i])*4 + int(n[i+1])*2 + int(n[i+2]))

print(number)