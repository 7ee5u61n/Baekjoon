n = int(input())
st = str(input())
for i in range(n):
    st[i:]
    if st[i:].count('s') == st[i:].count('t'):
        print(st[i:])
        break