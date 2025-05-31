n, m = map(int, input().split())
card = []
for _ in range(n):
    number = list(map(int, input().split()))
    number.sort(reverse=True)
    card.append(number)

player = [0]*(n)
for i in range(m):
    get = 0
    for j in range(n):
        get = max(card[j][i], get)

    for j in range(n):
        if card[j][i] == get:
            player[j] += 1

win = max(player)
for i in range(n):
    if player[i] == win:
        print(i+1, end=' ')