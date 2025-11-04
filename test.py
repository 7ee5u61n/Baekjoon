s = str(input())
k = str(input())

temp = ''
for i in s:
    if i.isalpha():
        temp += i

result = False
for i in range(len(temp)-len(k)+1):
    if temp[i:i+len(k)] == k:
        result = True
        break
        
if result:
    print(1)
else:
    print(0)