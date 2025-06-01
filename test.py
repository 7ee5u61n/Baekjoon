n, m, t = map(int, input().split())

burger = 0
coke = 10000

for i in range(t//n, -1, -1):
    for j in range(t//m, -1, -1):
        temp = t-(i*n+j*m)
        if coke > temp >= 0:
            burger = i+j
            coke = temp
        elif temp == coke:
            if i+j > burger:
                burger = i+j
                coke = temp
    
print(burger, coke)