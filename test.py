n, x = map(int, input().split())
t = list(map(int, input().split()))

index = 0
while True:
    if t[index] < x:
        break
    x += 1
    index = (index+1)%len(t)

print(index+1)