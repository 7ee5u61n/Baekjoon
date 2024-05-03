totalPrice = int(input())
while totalPrice < 1 or totalPrice > 1000000000:
    totalPrice = int(input())
kind = int(input())
while kind < 1 or kind > 100:
    kind = int(input())

itemCost = []
for i in range(kind):
    itemPrice, count = map(int, input().split())
    while itemPrice < 1 or itemPrice > 1000000 or count < 1 or count > 10:
        itemPrice, count = map(int, input().split())
    itemCost.append(itemPrice*count)

if sum(itemCost) == totalPrice:
    print('Yes')
else:
    print('No')