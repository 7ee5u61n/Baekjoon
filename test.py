n = int(input())

sm = 1/(7*24*60*60)
for i in range(1, n+1):
    sm*= i

print(int(sm))