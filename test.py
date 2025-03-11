n = int(input())
s = str(input())

hidden = ''
result = 0
for i in s:
    if i.isnumeric():
        hidden += i
    else:
        if hidden:
            result += int(hidden)
            hidden = ''
if hidden:
    result += int(hidden)
    
print(result)