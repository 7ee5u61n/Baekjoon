a, b, c, d = map(int, input().split())

shuttle = False
walk = False
if a+b <= d:
    shuttle = True
if c <= d:
    walk = True

if shuttle and walk:
    print('~.~')
elif shuttle:
    print('Shuttle')
elif walk:
    print('Walk')
else:
    print('T.T')