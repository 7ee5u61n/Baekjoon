while True:
    try:
        n, k = map(int, input().split())

        chicken = 0
        stamp = 0
        while True:
            if stamp >= k:
                n += stamp // k
                stamp %= k
            
            if n:
                chicken += n
                stamp += n
                n = 0
            else:
                break


        print(chicken)
    except EOFError:
        break