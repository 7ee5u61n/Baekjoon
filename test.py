ab = str(input())

if len(ab) == 2:
    a = int(ab[0])
    b = int(ab[1])
elif len(ab) == 4:
    a = int(ab[0:2])
    b = int(ab[2:4])
else:
    if ab[-1] == '0':
        a = int(ab[0])
        b = int(ab[1:3])
    else:
        a = int(ab[0:2])
        b = int(ab[2])
        
print(a+b)