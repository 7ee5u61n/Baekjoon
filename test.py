t, x = map(int, input().split())

n = int(input())

result = True
for _ in range(n):
    k = int(input())
    a = set(map(int, input().split()))
    
    if x not in a:
        result = False

if result:
    print("YES")
else:
    print("NO")