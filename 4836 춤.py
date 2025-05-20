while True:
    dance = input()
    
    if dance == '':
        break
    else:
        dance = dance.split()

    rule = {0: False, 1: True, 2: True, 3: True, 4: True, 5: True}

    twirl = False
    hop = False
    dip = False
    Dip = False
    for i in range(len(dance)):
        if i == 0:
            if dance[i] != 'jiggle':
                rule[4] = False
                
        if dance[i] == 'dip':
            rule[1] = True
            rule[5] = False
            dip = True
            try:
                if dance[i-1] == 'jiggle' or dance[i-2] == 'jiggle' or dance[i+1] == 'twirl':
                    rule[1] = False
                else:
                    dance[i] = 'DIP'
                    Dip = True
            except:
                dance[i] = 'DIP'
                Dip = True
        
        if dance[i] == 'twirl':
            twirl = True
        if dance[i] == 'hop':
            hop = True
    
    if not dip or not Dip:
        rule[1] = False
    else:
        rule[1] = True
    
    try:
        if dance[-3] == 'clap' and dance[-2] == 'stomp' and dance[-1] == 'clap':
            rule[2] = False
    except:
        rule[2] = True

    if twirl:
        if hop:
            rule[3] = False
    else:
        rule[3] = False

    wrong = []
    for i in range(1, 6):
        if rule[i] == True:
            wrong.append(i)
    
    print('form', end=' ')
    
    if wrong:
        if len(wrong) == 1:
            print(f'error {wrong[0]}:', end=' ')
        elif len(wrong) == 2:
            print(f'errors {wrong[0]} and {wrong[1]}:', end=' ')
        else:
            print('errors', end=' ')
            for i in range(len(wrong)):
                if i == len(wrong)-1:
                    print(f'and {wrong[i]}:', end=' ')
                elif i == len(wrong)-2:
                    print(f'{wrong[i]}', end=' ')
                else:
                    print(f'{wrong[i]},', end=' ')
    else:
        print('ok:', end=' ')
    
    for i in dance:
        print(i, end=' ')
    print()
