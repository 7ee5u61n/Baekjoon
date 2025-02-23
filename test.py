n = int(input())
for test_case in range(1, n+1):
    alphabet = [0]*26
    s = str(input())
    s = s.lower()

    for i in s:
        if i.isalpha():
            alphabet[ord(i)-97] += 1

    minNum = int(1e6)
    for i in alphabet:
        minNum = min(minNum, i)

    print(f'Case {test_case}:', end=' ')
    if minNum == 0:
        print('Not a pangram')
    elif minNum == 1:
        print('Pangram!')
    elif minNum == 2:
        print('Double pangram!!')
    else:
        print('Triple pangram!!!')