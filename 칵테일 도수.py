n = int(input())
st = str(input())

result = 0
for i in range(n//2):
    if st[i] != st[n-i-1]:
        result += 1

print(result)