n = int(input())

count = n
for i in range(2, int(n**0.5)+1):
    for j in range(i, n):
        if i*j<=n:
            count += 1
        else:
            break

print(count)