def iptoint(n):
    n = n.split('.')
    value = ''
    for i in range(8):
        x = str(bin(int(n[i])))[2:]
        while len(x) < 8:
            x = '0' + x
        value += x
    result = int(value, 2)
    
    return result

def inttoip(n):
    n = bin(int(n))[2:]
    while len(n) < 64:
        n = '0' + n
    value = ''
    for i in range(8):
        value += str(int(n[i*8:(i+1)*8], 2))
        if i < 7:
            value += '.'
    
    return value

n = int(input())

for i in range(n):
    m, n = map(str, input().split())
    if m == '1':
        print(iptoint(n))
    elif m == '2':
        print(inttoip(n))