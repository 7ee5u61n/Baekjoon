for i in range(10, 101):
    i = str(i)
    if int(i[::-1]) % 4 != 0:
        continue
    value = 0
    for j in range(len(i)):
        value += int(i[j])
    if value % 6 != 0:
        continue
    if i in '8':
        continue
    print(i)
    break
