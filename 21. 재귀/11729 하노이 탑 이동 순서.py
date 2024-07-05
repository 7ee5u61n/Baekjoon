count = 0
moving = []
def hanoi(disk, start, end, temp):
    global count

    if disk == 1:
        moving.append(start+" "+end)
        count += 1
    else:
        hanoi(disk - 1, start, temp, end)
        moving.append(start+ " "+end)
        hanoi(disk -1, temp, end, start)
        count += 1

hanoi(int(input()), '1', '3', '2')
print(count)
for i in moving:
    print(i)