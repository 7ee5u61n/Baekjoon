s = str(input())
arr = []
n = len(s)
for i in range(1, n-1):
    a = s[0:i]
    for j in range(1, n-i):
        b = s[i:i+j]
        c = s[i+j:]
        value = a[::-1] + b[::-1] + c[::-1]
        arr.append(value)

result = sorted(arr)[0]
print(result)