M = int(input())
D = int(input())

if M == 2 and D == 18:
    print('Special')
elif M == 2 and D < 18:
    print('Before')
elif M < 2:
    print('Before')
else:
    print('After')