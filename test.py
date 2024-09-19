N = int(input())

max_price = 0
for _ in range(N):
    dice = list(map(int, input().split()))
    dice.sort()
    same = len(set(dice))
    price = 0

    if same == 1:
        price = 50000 + dice[0] * 5000

    elif same == 2:
        if dice[1] == dice[2]:
            price = 10000 + dice[1] * 1000
        else:
            price = 2000 + dice[0] * 500 + dice[2] *500

    elif same == 3:
        same2 = 0
        for i in range(3):
            if dice[i] == dice[i+1]:
                same2 = dice[i]
                break
        
        price = 1000 + same2 * 100

    elif same == 4:
        price = max(dice) * 100

    if max_price < price:
        max_price = price

print(max_price)