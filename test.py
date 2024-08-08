MOBIS = {'M','O','B','I','S'}
S = set(input())

if set.intersection(S, MOBIS) == MOBIS:
    print('YES')
else:
    print('NO')