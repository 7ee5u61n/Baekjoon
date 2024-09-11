def AP(x, y, z):
    if z - y == y - x:
        return True
    else:
        return False

def GP(x, y, z):
    if z // y == y // x:
        return True
    else:
        return False
    
while True:
    a1, a2, a3 = map(int, input().split())
    if a1 == a2 == a3 == 0:
        break
    
    if AP(a1, a2, a3):
        print('AP',(a3 + (a2 - a1)))

    elif GP(a1, a2, a3):
        print('GP', (a3 * (a2 // a1)))