lv, judge = input().split()

if judge == 'miss':
    print(0)
elif judge == 'bad':
    print(int(lv) * 200)
elif judge == 'cool':
    print(int(lv) * 400)
elif judge == 'great':
    print(int(lv) * 600)
elif judge == 'perfect':
    print(int(lv) * 1000)