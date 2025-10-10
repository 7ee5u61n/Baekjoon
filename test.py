a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())

second = 0
if a < 0:
    frozen = True
else:
    frozen = False

while True:
    if a == b:
        break
    
    if a < 0:
        a += 1
        second += c
    elif a == 0 and frozen:
        frozen = False
        second += d
    else:
        a += 1
        second += e

print(second)
