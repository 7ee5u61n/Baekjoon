n = str(input())
result = False
for i in range(1, len(n)):
    a = n[:i]
    b = n[i:]
    front = 1
    back = 1
    for j in a:
        front *= int(j)
    for j in b:
        back *= int(j)

    if front == back:
        result = True
        break

if result:
    print("YES")
else:
    print("NO")