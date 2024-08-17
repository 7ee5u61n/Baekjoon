X = 0
Y = 0

N = int(input())
score = [input() for _ in range(N)]

for i in score:
    if i == 'D':
        X += 1
    else:
        Y += 1

    if abs(X-Y) == 2:
        break
    
print("%d:%d" %(X, Y))