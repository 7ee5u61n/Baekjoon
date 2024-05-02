a = int(input())
number2 = int(input())
b = []
while(number2!=0):
    b.append(number2%10)
    number2 = number2//10

print(a * b[0])
print(a * b[1])
print(a * b[2])