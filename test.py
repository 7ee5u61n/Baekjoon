n = int(input())
line = str(input())

result = True
for i in range(n*2-1):
    if line[i] == line[i+1]:
        result = False
        break

print("Yes" if result else "No")