test_case = 1
while True:
    n = int(input())
    if n == 0:
        break

    n1 = 3*n
    if n1 % 2 == 0:
        n2 = n1 // 2
    else:
        n2 = (n1 + 1) // 2
    
    n3 = 3*n2

    n4 = n3 // 9

    if n1 % 2 == 0:
        print(f'{test_case}. even {n4}')
    else:
        print(f'{test_case}. odd {n4}')

    test_case += 1