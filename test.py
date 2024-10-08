t = str(input())

key = ord(t[0])^ord('C')

s = ''
for i in t:
    s += chr(ord(i)^key)

print(s)