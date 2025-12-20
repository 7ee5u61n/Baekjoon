result = 0
n = int(input())

# 택희, 영훈, 남규
temp = 0
for i in range(2, n+1, 2):
    temp += i
    for j in range(1, n-i+1):
        temp += j
        for k in range(j+2, n-i-j+2):
            temp += k
            if temp == n:
                result += 1
            temp -= k
        temp -= j
    temp -= i

print(result)