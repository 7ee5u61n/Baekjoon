T = int(input())
for _ in range(T):
    c1, c2 = map(int, input().split())
    price = 0
    
    if 0 < c1 <= 1:
        price += 5000000
    elif 1 < c1 <= 3:
        price += 3000000
    elif 3 < c1 <= 6:
        price += 2000000
    elif 6 < c1 <= 10:
        price += 500000
    elif 10 < c1 <= 15:
        price += 300000
    elif 15 < c1 <= 21:
        price += 100000
    
    if 0 < c2 <= 1:
        price += 5120000
    elif 1 < c2 <= 3:
        price += 2560000
    elif 3 < c2 <= 7:
        price += 1280000
    elif 7 < c2 <= 15:
        price += 640000
    elif 11 < c2 <= 31:
        price += 320000

    print(price)