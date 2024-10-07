def trans(a, b):
    global t
    if a < b:
        return str(t[a])
    else:
        return trans(a//b, b) + str(t[a%b])
    
m, n = map(int, input().split())

t = '0123456789ABCDEF'

print(trans(m, n))