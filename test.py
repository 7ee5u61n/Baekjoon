m = int(input())
cocktail = {}

for i in range(m):
    s, x = input().split()
    x = int(x)
    if s in cocktail:
        cocktail[s] += x
    else:
        cocktail[s] = x

delicious = False
for i in range(len(cocktail)):
    for j in range(i + 1, len(cocktail)):
        s1 = list(cocktail.values())[i]
        s2 = list(cocktail.values())[j]
        if int(s1*1.618) == s2 or int(s2*1.618) == s1:
            delicious = True
            break

if delicious:
    print("Delicious!")
else:
    print("Not Delicious...")