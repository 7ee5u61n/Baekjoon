k = int(input())
s = str(input())
stack = []
char = s[0]
count = 0
for i in range(k):
    if s[i] == char:
        count += 1
    else:
        stack.append((char, count))
        char = s[i]
        count = 1
stack.append((char, count))

max_length = 0

for i in range(len(stack) - 1):
    char1, len1 = stack[i]
    char2, len2 = stack[i+1]

    if char1 != char2:
        max_length = max(max_length, min(len1, len2) * 2)

print(max_length)