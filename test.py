burgers = set()
beverage = set()

for _ in range(3):
    burgers.add(int(input()))

for _ in range(2):
    beverage.add(int(input()))

set = min(burgers) + min(beverage) - 50
print(set)