while True:
    s = str(input())
    if s == '*':
        break
    
    alphabet = set()
    for i in s:
        if i.isalpha():
            alphabet.add(i)
    
    if len(alphabet) == 26:
        print('Y')
    else:
        print('N')