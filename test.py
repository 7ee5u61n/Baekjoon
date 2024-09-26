d1, d2, d3 = map(int, input().split())
# a + b = d1, b + c = d2, a + c = d3
# b = d1 - a
# d1 - a + c = d2
# c = d2 - d1 + a
# c = d3 - a
# 0 = d2 - d1 + 2a + d3
a = (d1 + d2 - d3)/2
b = d1 - a
c = d2 - a

if a <= 0 or b <= 0 or c <= 0:
    print(-1)

else:
    print(1)
    print("%.1f %.1f %.1f" %(a, b, c))