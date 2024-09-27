import sys
N = list(map(int, sys.stdin.readline().rstrip()))
count2018 = {2:0, 0:0, 1:0, 8:0}

for i in N:
    try:
        count2018[i] += 1
    except:
        print(0)
        exit(0)

if count2018[2] != 0 and count2018[0] != 0 and count2018[1] != 0 and count2018[8] != 0:
    if count2018[2] == count2018[0] == count2018[1] == count2018[8]:
        print(8)
    else:
        print(2)
else:
    print(1)