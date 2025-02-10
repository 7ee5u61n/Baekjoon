n, m = map(int, input().split())
name = ''
m -= 1
if m // 26:
    name = chr(m//26+96)+chr(m%26+97)
else:
    name = chr(m%26+65)

print(f'SN {n}{name}')