n = int(input())
arr = list(map(str, input().split('*')))

left = arr[0]
right = arr[1]

for _ in range(n):
    name = str(input())

    if len(name) < len(left)+len(right):
        print('NE')
    else:
        if name[:len(left)] == left and name[-len(right):] == right:
            print('DA')
        else:
            print('NE')