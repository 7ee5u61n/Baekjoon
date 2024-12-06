n = int(input())

topping = list(map(str, input().split()))
cheese = set()

for i in topping:
    if len(i) >= 6:
        if i[-6:] == 'Cheese':
            cheese.add(i)

if len(cheese) >= 4:
    print('yummy')
else:
    print('sad')