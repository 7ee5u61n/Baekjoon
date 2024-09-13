N = int(input())
S = "%.300f" % 2 ** -N
end = len(S)
for i in range(end-1, 1, -1):
    if S[i] != '0':
        end = i
        break

print(S[:end+1])