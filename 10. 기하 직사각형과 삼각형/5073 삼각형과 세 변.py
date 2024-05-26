import sys
while True:
    l1 = 0
    l2 = 0
    l3 = 0
    length = []
    
    l1, l2, l3 = map(int, sys.stdin.readline().split())
    if l1 == l2 == l3 == 0:
        break
    length.append(l1)
    length.append(l2)
    length.append(l3)
    
    if max(length) >= l1 + l2 + l3 - max(length) :
        print('Invalid')
    elif l1 == l2 == l3:
        print('Equilateral')
    elif l1 == l2 or l2 == l3 or l3 == l1:
        print('Isosceles')
    elif l1 != l2 != l3 != l1:
        print('Scalene')