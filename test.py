n = int(input())

k = 64
while True:
    if n%2 == 1:
        break
    else:
        n//=2
    k -= 1

print(k)