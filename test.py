mushroom = [int(input()) for _ in range(10)]
point = 0
for i in range(10):
    if point + mushroom[i] >= 100:
        if abs(100-point) >= abs(100-(point+mushroom[i])):
            point += mushroom[i]
        break
    point += mushroom[i]

print(point)