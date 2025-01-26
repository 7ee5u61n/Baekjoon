n = int(input())
x = list(map(int, input().split()))

group = []
temp = [x[0]]
for i in range(1, n):
    if x[i] - x[i-1] == 1:
        temp.append(x[i])
    else:
        group.append(temp)
        temp = [x[i]]
    
if temp:
    group.append(temp)

result = 0
for part in group:
    result += part[0]

print(result)