N = int(input())
P = int(input())

if N >= 20:
    if P >= 8000:
        P *= 0.75
    else:
        P -= 2000

elif N >= 15:
    if P >= 20000:
        P *= 0.9
    else:
        P -= 2000

elif N >= 10:
    if P >= 5000:
        P *= 0.9
    else:
        P -= 500

elif N >= 5:
    P -= 500

if P < 0:
    P = 0

print(int(P))