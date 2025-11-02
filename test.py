n = int(input())

arr1 = []
for i in range(n):
    arr1.append(int(input()))

arr2 = sorted(arr1)

if arr1[0] == arr2[0]:
    print('ez')
elif arr1[0] == arr2[-1]:
    print('hard')
else:
    print('?')