n, m, s = map(int, input().split())

a = int(s*(m+1)*(100-n)/100)
b = s*m

print(min(a, b))