n = int(input())

if n % 16 == 1 or n % 16 == 9:
    print(1)
elif n % 16 == 2 or n % 16 == 8 or n % 16 == 10 or n % 16 == 0:
    print(2)
elif n % 16 == 3 or n % 16 == 7 or n % 16 == 11 or n % 16 == 15:
    print(3)
elif n % 16 == 4 or n % 16 == 6 or n % 16 == 12 or n % 16 == 14:
    print(4)
elif n % 16 == 5 or n % 16 == 13:
    print(5)

