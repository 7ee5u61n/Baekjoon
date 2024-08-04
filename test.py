number = str(input())

sum = 0
for i in range(len(number)):
    if 65<=ord(number[i])<=70:
        sum += (ord(number[i])-55)*(16**(len(number)-i-1))
    else:
        sum += int(number[i])*(16**(len(number)-i-1))

print(sum)