T = int(input())
for _ in range(T):
    input()
    cm, y, su, sa, f = map(int, input().split())
    b, gs, gc, w = map(int, input().split())

    dough = int(min(cm/8, y/8, su/4, sa/1, f/9)*16)
    
    banana = min(dough, b)
    dough -= banana
    strawberry = min(dough, gs//30)
    dough -= strawberry
    chocolate = min(dough, gc//25)
    dough -= chocolate
    walnut = min(dough, w//10)

    print(banana+strawberry+chocolate+walnut)