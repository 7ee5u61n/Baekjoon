n, m = map(int, input().split())

package = 1000
each = 1000
# 가장 싼 패키지와 낱개
for _ in range(m):
    a, b = map(int, input().split())
    package = min(a, package)
    each = min(b, each)

# 낱개로 사는 것이 더 쌀 때
if each*6 <= package:
    print(each*n)
else:
    # 패키지로 전부 구입
    if n % 6 == 0:
        print(package*(n//6))
    # 패키지 + 낱개와 패키지로 초과 구매 중 작은 거
    else:
        print(min(package*(n//6)+each*(n%6), (package*(n//6+1))))
