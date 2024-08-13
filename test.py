n, T = map(int, input().split())
work = list(map(int, input().split()))
sum = 0
count = 0
while count < n:
    sum += work.pop(0)
    if sum > T:
        break
    count += 1
print(count)