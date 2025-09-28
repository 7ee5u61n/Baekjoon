n, a, b = map(int, input().split())

o1, o2 = 1, 1

switch = True
for i in range(n):
    if switch:
        o1 += a
        o2 += b
        
        if o1 < o2:
            switch = False
        elif o1 == o2:
            o2 -= 1

    else:
        o1 += b
        o2 += a

        if o2 < o1:
            switch = True
        elif o1 == o2:
            o1 -= 1

if switch:
    print(o1, o2)
else:
    print(o2, o1)