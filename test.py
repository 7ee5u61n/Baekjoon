S = str(input())
K = str(input())

E = ''
for i in S:
    if i.isalpha():
        E += i
        
if K in E:
    print(1)
else:
    print(0)