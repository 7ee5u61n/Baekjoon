def numeral(num, base):
    result = ''
    while num >= base:
        result += str(num%base)
        num //= base
    result += str(num)
    
    return(result[::-1])

while True:
    arr = list(map(int, input().split()))
    if arr[0] == 0:
        break

    b, p, m = arr[0], arr[1], arr[2]

    n = int(str(p), b) % int(str(m), b)
    
    print(numeral(n, b))