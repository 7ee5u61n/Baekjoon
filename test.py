n = int(input())

weather = list(map(int, input().split()))

result = [0]
for i in weather:
    if i:
        result.append(result[-1]+1)
    else:
        result.append(result[-1]-1)

print(sum(result))