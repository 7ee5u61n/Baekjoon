n = int(input())
k = str(input())

odd = 0
even = 0
for i in range(n):
    if int(k[i]) % 2 == 0:
        even += 1
    else:
        odd += 1

if even > odd:
    print(0)
elif odd > even:
    print(1)
else:
    print(-1)