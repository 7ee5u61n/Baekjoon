import string

N = int(input())

for _ in range(N):
    alphabet = dict.fromkeys(string.ascii_lowercase, 0)
    S = str(input())
    S = S.lower()

    for i in S:
        if i in alphabet:
            alphabet[i] += 1

    missing = ''
    for j in alphabet:
        if alphabet[j] == 0:
            missing += j

    if missing:
        print(f'missing {missing}')
    else:
        print('pangram')