bowl = list(input())
height = 0
last = ''

for i in range(len(bowl)):
    if bowl[i] == last:
        height += 5
    else:
        height += 10
    last = bowl[i]

print(height)