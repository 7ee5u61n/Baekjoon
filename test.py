arr = list(map(int, input().split()))

if arr == sorted(arr):
    print('Good')
else:
    print('Bad')