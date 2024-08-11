kilogram = 2.2046  #lb
pound = 0.4536 #kg
liter = 0.2642 #g
galon = 3.7854 #l

T = int(input())

for i in range(T):
    number, unit = input().split()
    number = float(number)
    if unit == 'kg':
        print(str(f"{number*kilogram:.4f}"),'lb')
    elif unit == 'lb':
        print(str(f"{number*pound:.4f}"),'kg')
    elif unit == 'l':
        print(str(f"{number*liter:.4f}"),'g')
    elif unit == 'g':
        print(str(f"{number*galon:.4f}"),'l')