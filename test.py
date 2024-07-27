N = int(input())
for i in range(N):
    password = str(input())
    if len(password) <= 9 and len(password) >= 6:
        print('yes')
    else:
        print('no')