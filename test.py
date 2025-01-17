import math

test_case = 1
while True:
    arr = list(map(int, input().split()))
    if arr[0] == 0:
        break
    
    r = arr[0]
    w = arr[1]
    l = arr[2]

    if math.sqrt(w**2+l**2)/2 <= r:
        print(f'Pizza {test_case} fits on the table.')
    else:
        print(f'Pizza {test_case} does not fit on the table.')

    test_case += 1