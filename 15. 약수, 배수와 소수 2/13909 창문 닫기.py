def sqrt_N(x): # X 보다 작은 제곱수 찾는 함수
    count = 0
    x = 1
    while x*x <= N:
        x += 1
        count += 1
    return count

N = int(input())

print(sqrt_N(N))