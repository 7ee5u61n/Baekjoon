order = str(input())

robot = 0
box = 0
goal = 0

for i in range(len(order)):
    if order[i] == '@':
        robot = i
    elif order[i] == '#':
        box = i
    elif order[i] == '!':
        goal = i

if robot < box < goal:
    print(goal - robot - 1)
elif robot > box > goal:
    print(robot - goal - 1)
else:
    print(-1)