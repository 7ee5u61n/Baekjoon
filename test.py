socks = [0]*10

for i in range(5):
    n = int(input())
    socks[n] += 1

for i in range(10):
    if socks[i] % 2 == 1:
        print(i)
        break