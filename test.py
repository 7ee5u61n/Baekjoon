while True:
    try:
        n = int(input())
    except:
        break

    count = 1
    number = set()
    while True:
        temp = n * count
        for digit in str(temp):
            number.add(int(digit))
        if len(number) == 10:
            break
        count += 1

    print(count)