n, m, k = map(int, input().split())

mn = max(n-(m*k), 0)
mx = n-m*(k-1)-1

print(mn, mx)