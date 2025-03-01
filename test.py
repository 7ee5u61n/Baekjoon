n = int(input())
s = str(input())
# 25자 이내
if n <= 25:
    print(s)
else:
    rest = s[11:-11]
    # 한 문장 안
    if '.' not in rest[:-1]:
        rest = '...'
        print(s[:11]+rest+s[-11:])
    else:
        rest = '......'
        print(s[:9]+rest+s[-10:])