point = [100, 100, 200, 200, 300, 300, 400, 400, 500]
solve = list(map(int, input().split()))

isHacker = False
total = 0
for i in range(9):
    if solve[i] > point[i]:
        isHacker = True
        break
    total += solve[i]

if isHacker:
    print("hacker")
else:
    if total >= 100:
        print("draw")
    else:
        print("none")