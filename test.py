T = 1
block = [[], ['4', '5'], [], ['4', '5'], ['2', '3'], 
         ['8'], ['2', '3'], ['8'], ['6', '7']]
while True:
    n = str(input())
    if n == '0':
        break

    valid = True
    if n[0] == '1' and n[-1] == '2':
        for i in range(len(n)-1):
            if n[i+1] not in block[int(n[i])]:
                valid = False
                break
    else:
        valid = False

    if valid:
        print(f'{T}. VALID')
    else:
        print(f'{T}. NOT')
    T += 1