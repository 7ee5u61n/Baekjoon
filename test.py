a, b = map(int, input().split())
c, d = map(int, input().split())

gadong = 1
for i in range(a+b-1):
    gadong += 1
    if gadong > 4:
        gadong = 1

jindong = int(gadong)
for i in range(c+d-1):
    jindong += 1
    if jindong > 4:
        jindong = 1

print(jindong)