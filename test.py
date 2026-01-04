n = str(input())

result = 0
while len(n) > 1:
    sum_digits = 1
    for digit in n:
        sum_digits *= int(digit)
    result += 1
    n = str(sum_digits)

print(result)
