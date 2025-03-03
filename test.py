import math

d, h, w = map(int, input().split())

value = d/math.sqrt(h**2+w**2)
rH = int(h*value)
rW = int(w*value)

print(rH, rW)