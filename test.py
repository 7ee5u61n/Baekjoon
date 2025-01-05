n = int(input())
mahjong = list(map(str, input().split()))

card = {'1m':0, '2m':0, '3m':0, '4m':0, '5m':0, '6m':0, '7m':0, '8m':0, '9m':0, 
    '1p':0, '2p':0, '3p':0, '4p':0, '5p':0, '6p':0, '7p':0, '8p':0, '9p':0,
    '1s':0, '2s':0, '3s':0, '4s':0, '5s':0, '6s':0, '7s':0, '8s':0, '9s':0,
    '1z':0, '2z':0, '3z':0, '4z':0, '5z':0, '6z':0, '7z':0}

result = 0
for i in range(n):
    card[mahjong[i]] += 1
    if card[mahjong[i]] == 5:
        result = i+1
        break

print(result)