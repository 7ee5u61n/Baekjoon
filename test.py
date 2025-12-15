a = int(input())
b = int(input())
c = int(input())

abc = str(a * b * c)

result = [0]*10
for i in abc:
    result[int(i)] += 1

for i in range(10):
    print(result[i])