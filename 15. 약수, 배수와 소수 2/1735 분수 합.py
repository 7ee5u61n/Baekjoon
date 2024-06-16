def GCD(x, y): # 최대공약수
    while(y):
        x, y = y, x % y
    return x

def LCM(x, y): # 최소공배수
    result = (x * y) // GCD(x, y)
    return result

numer1, denom1 = map(int, input().split())
numer2, denom2 = map(int, input().split())

numer = numer1 * denom2 + numer2 * denom1
denom = denom1 * denom2

if GCD(numer ,denom) == 1:
    print(numer, denom)
else: # 분자와 분모의 최소공배수가 1이 아닐때, 약분할 수 있을 때
    last_numer = numer // GCD(numer, denom)
    last_denom = denom // GCD(numer, denom)
    print(last_numer, last_denom)