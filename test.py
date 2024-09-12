L = int(input())
order = str(input())

location = [0, 0]
visited = [[0, 0]]
for i in range(L):
    if order[i] == 'E':
        location[0] += 1
    elif order[i] == 'W':
        location[0] -= 1
    elif order[i] == 'S':
        location[1] -= 1
    elif order[i] == 'N':
        location[1] += 1

    if location not in visited:
        visited.append(location[:])

print(len(visited))