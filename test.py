r, g, b = map(int, input().split())

r2 = r/255
g2 = g/255
b2 = b/255
k = 1 - max(r2, g2, b2)

if k == 1:
    c = 0
    m = 0
    y = 0
else:
    c = (1 - r2 - k) / (1 - k)
    m = (1 - g2 - k) / (1 - k)
    y = (1 - b2 - k) / (1 - k)

print(c, m, y, k)