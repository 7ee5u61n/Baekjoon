n, m = map(int, input().split())
t, s = map(int, input().split())

zip = n+(n-1)//8*s
dok = t+m+(m-1)//8*(2*t+s)

if zip > dok:
    print('Dok')
    print(dok)
else:
    print('Zip')
    print(zip)