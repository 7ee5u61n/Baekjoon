x, y, w, h = map(int, input().split())

distance = [w-x, x, h-y, y]
print(min(distance))