import sys

case = 1
while True:
    o, w = map(int, input().split())
    if o == 0 and w == 0:
        break
    RIP = False
    
    while True:
        ef, n = input().split()
        if ef == '0' and n == '0':
            break

        if ef == 'E':
            w -= int(n)
        else:
            w += int(n)

        if w <= 0:
            RIP = True

        if ef == '#' and n == '0':
            if RIP:
                print(case, 'RIP')
            elif (o*0.5) < w < (o*2):
                print(case, ':-)')
            else:
                print(case, ':-(')
            break
    case += 1