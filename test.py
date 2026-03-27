n = int(input())

arr = [0]*3
vote = list(map(int, input().split()))

for i in vote:
    if i == 1:
        arr[0] += 1
    elif i == -1:
        arr[1] += 1
    else:
        arr[2] += 1

if arr[2] >= n/2:
    print('INVALID')
else:
    if arr[0] > arr[1]:
        print('APPROVED')
    else:
        print('REJECTED')