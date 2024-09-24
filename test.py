# 1, 3, 6, 10, 15, 21, 28
# 1 = W, 2 = W, 3 = L
N = int(input())

count = 0
for i in range(1, 100001):
    if count > N:
        break

    count += i
    
if i % 2 == 0:
    print(count - N)
else:
    print(0)