k, d, a = map(int, input().split('/'))

flag = True

if k+a < d or d == 0:
    flag = False

if flag:
    print('gosu')
else:
    print('hasu')