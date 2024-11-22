n = int(input())
sell = {}
for _ in range(n):
    book = str(input())
    if book in sell:
        sell[book] += 1
    else:
        sell[book] = 1

bestSeller = []

for key, value in sell.items():
    if value == max(sell.values()):
        bestSeller.append(key)

bestSeller.sort()

print(bestSeller[0])