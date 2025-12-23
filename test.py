n = int(input())

arr = [i for i in range(1, n+1)]

while len(arr) > 1:
    arr = [arr[i] for i in range(1, len(arr), 2)]

print(arr[0])