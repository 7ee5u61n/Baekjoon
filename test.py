n = int(input())
A, B, C, D = map(int, input().split())
s = input()

stack = 0
if s[0] == 'a' and s[-1] == 'a':
    for i in range(n):
        if s[i] == 'a':
            A -= 1
        elif s[i] == 'b':
            B -= 1
        elif s[i] == 'c':
            C -= 1
        elif s[i] == 'd':
            D -= 1

        if i != n-1:
            if s[i] == s[i+1]:
                break

        stack += 1

if stack == n and A >= 0 and B >= 0 and C >= 0 and D >= 0:
    print('Yes')
else:
    print('No')