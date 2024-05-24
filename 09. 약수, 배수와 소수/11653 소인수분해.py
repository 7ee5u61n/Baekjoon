N = int(input())
if N == 1:
    exit

def prime_factor(n): # 소인수분해 하는 알고리즘
    answer = []
    x = 2
    while x <= n:
        if n % x == 0:
            answer.append(x)
            n //= x
        else:
            x += 1
    return answer

result = prime_factor(N)
for i in range(len(result)):
    print(result[i])