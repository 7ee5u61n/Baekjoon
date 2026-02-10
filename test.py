def factorial(n):
    sum = 1
    for i in range(1, n+1):
        sum *= i
    if n == 0:
        return 1
    else:
        return sum
    
print('n e')
print('- -----------')
sum = 0
for i in range(10):
    sum += 1 / factorial(i)
    if i < 2:
        print(i, int(sum))
    elif i == 2:
        print(i, float(sum))
    else:
        print(i, '{0:.9f}'.format(sum))