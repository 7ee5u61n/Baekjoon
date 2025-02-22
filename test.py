T = int(input())
for _ in range(T):
    S = str(input())
    if len(S)%3 == 0:
        s = S[:len(S)//3]
    else:
        s = S[:len(S)//3+1]

    three = False
    if S == s+s[::-1]+s:
        three = True
    elif S == s+(s[::-1])[1:]+s:
        three = True
    elif S == s+s[::-1]+s[1:]:
        three = True
    elif S == s+(s[::-1])[1:]+s[1:]:
        three = True

    if three:
        print(1)
    else:
        print(0)