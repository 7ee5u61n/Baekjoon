q = int(input())
problem = 0
adios = False
for _ in range(q):
    a, b = map(int, input().split())
    if a == 1:
        problem += b
    elif a == 2:
        problem -= b

    if problem < 0:
        adios = True

if adios:
    print('Adios')
else:
    print('See you next month')