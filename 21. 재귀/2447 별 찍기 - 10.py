def star(N):
    if N == 3:
        return ['*'*3, '*'+' '+'*', '*'*3]
    lenth = star(N//3);
    stars = []
        
    for i in lenth:
        stars.append(i*3)
    for i in lenth:
        stars.append(i+' '*(N//3)+ i)
    for i in lenth:
        stars.append(i*3)
    return stars

N = int(input())
print(*star(N), sep='\n')