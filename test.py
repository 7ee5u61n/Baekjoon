n = int(input())

for k in range(64, -1, -1):
    if n%2 == 1:
        break
    else:
        n//=2

print(k)