def solve(s):
    value = 0
    for i in s:
        if i.isupper():
            value += 4
        elif i.islower():
            value += 2
        elif i.isdigit():
            value += 2
        elif i == ' ':
            value += 1
    
    return value

j, n = map(int, input().split())

result = 0
for _ in range(n):
    s = input()

    if solve(s) <= j:
        result += 1

print(result)