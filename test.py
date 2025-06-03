n = int(input())

for i in range(n):
    usG, usS, usB, rusG, rusS, rusB = map(int, input().split())

    count = False
    color = False
    
    if usG+usS+usB > rusG+rusS+rusB:
        count = True
    
    if usG > rusG:
        color = True
    elif usG == rusG:
        if usS > rusS:
            color = True
        elif usS == rusS:
            if usB > rusB:
                color = True

    print(usG, usS, usB, rusG, rusS, rusB)
    
    if count and color:
        print('both')
    elif count:
        print('count')
    elif color:
        print('color')
    else:
        print('none')
    
    print()