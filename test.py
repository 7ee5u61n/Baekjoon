geminis = list(map(int, input().split()))
gullivers = list(map(int, input().split()))
a = 0
b = 0
counter = False
for i in range(9):
    a += geminis[i]
    if a > b:
        counter = True
    b += gullivers[i]
    if a > b:
        counter = True

if counter and a < b:
    print('Yes')
else:
    print('No')