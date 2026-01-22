s1 = str(input())
s2 = str(input())
s3 = str(input())

glob = ['l', 'k', 'p']

result = False
if s1[0] in glob:
    glob.remove(s1[0])
    if s2[0] in glob:
        glob.remove(s2[0])
        if s3[0] in glob:
            glob.remove(s3[0])
            result = True

if result:
    print("GLOBAL")
else:
    print("PONIX")