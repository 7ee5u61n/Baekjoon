import math

while True:
    n = list(str(input()))
    if n == ['0']:
        break
    
    palindrome = True
    for i in range(math.floor(len(n)/2)):
        if n[i] != n[-1-i]:
            palindrome = False
            break
    if palindrome == True:
        print('yes')
    else:
        print('no')