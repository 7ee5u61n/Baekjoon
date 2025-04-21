n = int(input())
a, pa, b, pb = map(int, input().split())

tank = 0
dps = 0

for x in range(n//pa+1):
    y = (n-pa*x)//pb
    if a*tank + b*dps < a*x+b*y:
        tank = x
        dps = y

print(tank, dps)