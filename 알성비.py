n = int(input())

result = ''
for _ in range(n):
    name = str(input())
    
    if 'S' in name:
        result = name

print(result)