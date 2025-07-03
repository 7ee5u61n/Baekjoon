def check(n):
    base10 = 0
    for i in n:
        base10 += int(i)
    base12 = 0
    for i in solution(int(n), 12):
        if i == 'a':
            base12 += 10
        elif i == 'b':
            base12 += 11
        else:
            base12 += int(i)
        
    base16 = 0
    for i in solution(int(n), 16):
        if i == 'a':
            base16 += 10
        elif i == 'b':
            base16 += 11
        elif i == 'c':
            base16 += 12
        elif i == 'd':
            base16 += 13
        elif i == 'e':
            base16 += 14
        elif i == 'f':
            base16 += 15
        else:
            base16 += int(i)

    if base10 == base12 == base16 == base10:
        return True
    
def solution(n, base):
    value = ''
    while n > 0:
        n, mod = divmod(n, base)
        if mod == 10:
            value += 'a'
        elif mod == 11:
            value += 'b'
        elif mod == 12:
            value += 'c'
        elif mod == 13:
            value += 'd'
        elif mod == 14:
            value += 'e'
        elif mod == 15:
            value += 'f'
        else:
            value += str(mod)
    
    return value[::-1]

for i in range(1000, 10000):
    if check(str(i)):
        print(i)