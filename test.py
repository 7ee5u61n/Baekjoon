import math

n, m, a, k = map(int, input().split())

low = min(n, a-k+1)
high = math.ceil((a-k)/m)+1

print(low, high)