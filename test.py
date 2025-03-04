octopus = {'-':0, '\\':1, '(':2, '@':3, '?':4, '>':5, '&':6, '%':7, '/':-1}

while True:
    s = str(input())
    if s == '#':
        break
    value = 0
    for i in range(len(s)):
        value += octopus[s[i]]*(8**(len(s)-i-1))

    print(value)