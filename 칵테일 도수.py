n = int(input())
arr = list(map(int, input().split()))
set_arr = set(arr)

if len(arr) == len(set_arr):
    print(1)
else:
    print(0)