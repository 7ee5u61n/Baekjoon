def GCD(x, y): # 최대공약수
    while(y):
        x, y = y, x % y
    return x

def LCM(x, y): # 최소공배수
    result = (x * y) // GCD(x, y)
    return result

a, b = map(int, input().split())

print(GCD(a, b))
print(LCM(a, b))