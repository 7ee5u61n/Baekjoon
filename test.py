n = int(input())
seat = list(input())

couple = 0
stack = ''
for i in range(n):
    stack += seat[i]
    if 'LL' in stack:
        couple += 1
        stack = ''

if couple:
    result = n-(couple-1)
else:
    result = n
    
print(result)