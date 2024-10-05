n, m = map(int, input().split())
count = n
while n:
    n //= m
    count += n

print(count)