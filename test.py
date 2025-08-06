while True:
    code = str(input())
    if code == 'END':
        break
    print(code[::-1])