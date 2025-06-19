T = int(input())
for _ in range(T):
    g, c, e = map(int, input().split())
    if g == 1:
        g = 1
    elif g == 2:
        g = 3
    elif g == 3:
        g = 5
        
    if c >= e:
        result = 0
    else:
        result = (e - c) * g
    
    print(result)