def is_prime(n):
    end = int(n**(0.5))
    for i in range(2, end+1):
        if n % i == 0:
            return False
    return True

n = int(input())

for i in range(n, int(1e9)+1):
    if is_prime(i) == False:
        print(i)
        break