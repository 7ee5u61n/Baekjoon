pi = 3.141592
i = 1
while True:
    miles, rpm, time = map(float, input().split())

    if rpm == 0:
        break
    
    distance = miles/63360*pi*rpm
    mph = distance / time * 3600

    print('Trip #%d: %.2f %.2f' %(i, distance, mph))
    i += 1