n = int(input())
size = list(map(int, input().split()))
t, p = map(int, input().split())

tshirts = 0
for i in range(6):
    tshirts += size[i] // t
    if size[i] % t:
        tshirts += 1

print(tshirts)
print(n//p, n%p)