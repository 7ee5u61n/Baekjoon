s = str(input())

result = 0
point = 1
for i in range(len(s)-1):
    if ord(s[i]) < ord(s[i+1]):
        result += point
        point += 1
    else:
        result += point
        point = 1
    
result += point
print(result)