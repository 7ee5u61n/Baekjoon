K = int(input())

for i in range(K):
    h = int(input())
    act = str(input())
    
    for j in range(len(act)):
        if h == 0:
            break
        
        if act[j] == 'c':
            h += 1
        else:
            h -= 1

    print('Data Set', str(i+1) +':')
    print(str(h)+('\n'))