x = int(input())

y = -1
for i in range(x+1, 10000):
    front = int(str(i)[0:2])
    back = int(str(i)[2:4])

    if (front+back)**2 == i:
        y = i
        break

print(y)