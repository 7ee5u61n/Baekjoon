jaesoo = input()
n = int(input())

count = 0
for _ in range(n):
    code = input()
    if code[0:5] == jaesoo[0:5]:
        count += 1

print(count)